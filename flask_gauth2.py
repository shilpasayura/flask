import json
import flask
import httplib2
from googleapiclient import discovery
from oauth2client import client
# from imaplib import USER


app = flask.Flask(__name__)

# Create 'client_secret.json from API manager + credential from:
# https://console.developers.google.com/project
# The scopes are listed in:
# https://developers.google.com/identity/protocols/googlescopes#oauth2v2

CLIENT_SECRETS_FILE = 'secrets/client_secrets_google.json'
SCOPE = 'https://www.googleapis.com/auth/userinfo.profile'


# The content of the returned values of the API are set in:
# https://developers.google.com/apis-explorer/?hl=en_US#p/

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
    """
    See http://blog.miguelgrinberg.com/post/oauth-authentication-with-flask
    on how different providers can be handled in Flask.
    Here only google is handled
    """
    return 'google'


@app.route('/')
@app.route('/index')
def index():
    
    if 'credentials' not in flask.session:
        return flask.redirect(flask.url_for(
                'oauth_callback',
                provider=get_provider())
                )
    credentials = client.OAuth2Credentials.from_json(
                    flask.session['credentials']
                    )
    if credentials.access_token_expired:
        return flask.redirect(flask.url_for(
                             'oauth_callback',
                             provider=get_provider())
                              )
    else:
        http_auth = credentials.authorize(httplib2.Http())
        service = discovery.build(API_SERVICE,
                                  API_SERVICE_VERSION,
                                  http=http_auth)
        userinfo = handleAPI(service)
        print(userinfo['name'])
        return json.dumps(userinfo)


@app.route('/callback')
@app.route('/callback/<provider>')
def oauth_callback(provider):
    flow = client.flow_from_clientsecrets(
        CLIENT_SECRETS_FILE,
        scope=SCOPE,
        redirect_uri=flask.url_for('oauth_callback',
                                   provider=get_provider(),
                                   _external=True)
        )
    if 'code' not in flask.request.args:
        auth_uri = flow.step1_get_authorize_url()
        return flask.redirect(auth_uri)
    else:
        auth_code = flask.request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        flask.session['credentials'] = credentials.to_json()
        return flask.redirect(flask.url_for('index'))


if __name__ == '__main__':
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.run(host='0.0.0.0',port=8000)


