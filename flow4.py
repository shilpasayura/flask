import flask
import httplib2
import json
#from oauth2client.client import OAuth2WebServerFlow
from oauth2client import client
from googleapiclient import discovery

app = flask.Flask(__name__)

API_SERVICE = 'oauth2'
API_SERVICE_VERSION = 'v2'

def handleAPI(service):
    """
    The method supported by the OAuth2A API are described in:
    https://google-api-client-libraries.appspot.com/documentation/oauth2/v2/python/latest/index.html
    Here could use different providers or services
    """
    return service.userinfo().get().execute()

def get_provider():
    return 'google'
  
def logdata(content,file, op):
  f = open(file, op);
  f.write(content)
  f.close()
  
def dump_obj(obj):  
  for attr in dir(obj):
    print (attr)


@app.route('/')
@app.route('/index')
def index():
    
    if 'credentials' not in flask.session:
        print("No Credentials - redirecting")
        return flask.redirect(flask.url_for(
                'oauth_callback',
                provider=get_provider())
                )

    credentials = client.OAuth2Credentials.from_json(
                    flask.session['credentials']
                    )
    print(credentials)
    
    if credentials.access_token_expired:
        print("Expired")
        return flask.redirect(flask.url_for(
                             'oauth_callback',
                             provider=get_provider())
                              )
    else:
        print("Authorising Credentials")
        http_auth = credentials.authorize(httplib2.Http())
        service = discovery.build(API_SERVICE,
                                  API_SERVICE_VERSION,
                                  http=http_auth)
        userinfo = handleAPI(service)
        print(userinfo['name'])
        return json.dumps(userinfo)
      
  
@app.route('/callback')
@app.route('/callback/<provider>') # provider is a parameter
def oauth_callback(provider):
  
  #rd_uri=flask.url_for('oauth_callback',provider=get_provider(),_external=True)

  flow = client.OAuth2WebServerFlow(client_id='96319319647-76o10sfifhhthldd6avh8p7l83vplqtq.apps.googleusercontent.com',
                           client_secret='hSA3d2SUN7HqnAkH9oR3joki',
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='http://localhost:8000/callback/google')

  '''
    
    flow = flow_from_clientsecrets('secrets/client_secrets_google.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://localhost/callback/google')
    '''

  if 'code' not in flask.request.args:
    print("no code - redirecting")
    auth_uri = flow.step1_get_authorize_url()
    return flask.redirect(auth_uri)
  else:
    
    auth_code = flask.request.args.get('code')
    credentials = flow.step2_exchange(auth_code)
    flask.session['credentials'] = credentials.to_json()
    print("Got credentials", flask.session['credentials'])
    return flask.redirect(flask.url_for('index'))
      
  
if __name__ == '__main__':
  app.secret_key = 'secRET4566'
  app.run(host='0.0.0.0',port=8000)
