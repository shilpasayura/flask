import flask
import httplib2
import json
from oauth2client.client import OAuth2WebServerFlow



def logdata(content,file, op):
  f = open(file, op);
  f.write(content)
  f.close()
  
def dump_obj(obj):  
  for attr in dir(obj):
    print (attr)
    #print(getattr(obj, attr))
'''   
def getcode(response):
  q = urlparse(response)
  q_components = dict(qc.split("=") for qc in q.split("&"))
  print(q_components)
'''  

def get_provider():
    return 'google'
  
app = flask.Flask(__name__)


@app.route('/')
def login():

    rd_uri=flask.url_for('oauth_callback',provider=get_provider(),_external=True)
    print(rd_uri)
    
    flow = OAuth2WebServerFlow(client_id='96319319647-76o10sfifhhthldd6avh8p7l83vplqtq.apps.googleusercontent.com',
                           client_secret='hSA3d2SUN7HqnAkH9oR3joki',
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='http://localhost:8000/callback/google')
   
    '''
    flow = flow_from_clientsecrets('secrets/client_secrets_google.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://localhost/callback/google')
    '''
    
    authorization_url = flow.step1_get_authorize_url()
    http=httplib2.Http()
    response, content = http.request(authorization_url)


    # Store the state so the callback can verify the auth server response.
    #flask.session['state'] = response

    ''' 
    #http://localhost/callback/google?code=4/RwDQKS_RHED7Ux1o67I8Lbt-olOr2FA ....
    if response.status == 200:
       print ("response . content-type", response["content-type"])
       d = self.reflector(content)
       s=content.decode("UTF-8")
       #logdata(s, "logc.txt", 'w+')
       print(s)
       
    print(type(response), type(content))
    logdata(content, "logfile.txt", 'wb+')

    '''
    

    #flask.session['credentials'] = credentials_to_dict(credentials)
    
      
    return content

@app.route('/hi')
def hi():
  return "BOOOOO"
  
@app.route('/callback')
@app.route('/callback/<provider>') # provider is a parameter
def oauth_callback(provider):
  
  #auth_response = flask.request.url
  auth_code = flask.request.args.get('code')
  print(auth_code)

  #resp_arr=httplib2.parse_uri(auth_response)
  credentials = flow.step2_exchange(auth_code)
  #flask.session['credentials'] = credentials.to_json()
  x=credentials.to_json()
  #return flask.redirect(flask.url_for('index'))

  print (x)
  return "helloooooooooooooo"
  
if __name__ == '__main__':
  app.secret_key = 'secRET4566'
  app.run(host='0.0.0.0',port=8000)

'''
print(auth_uri)

credentials = flow.step2_exchange(code)
# Redirect the user to auth_uri on your platform.

import httplib2

http = httplib2.Http()
http = credentials.authorize(http)


from apiclient.discovery import build

service = build('calendar', 'v3', http=http)

'''
