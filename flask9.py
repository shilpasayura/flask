from flask import Flask, redirect, url_for, session
from authlib.flask.client import OAuth
import ssl
 
 
# Configure values from Google APIs console
# https://code.google.com/apis/console
#GOOGLE_CLIENT_ID = 'PUT CLIENT ID'
#GOOGLE_CLIENT_SECRET = 'PUT CLIENT SECRET'

GOOGLE_CLIENT_ID = '96319319647-76o10sfifhhthldd6avh8p7l83vplqtq.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'hSA3d2SUN7HqnAkH9oR3joki'




REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console
 
SECRET_KEY = 'development7key'
DEBUG = True
 
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()
 
google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)
 
@app.route('/')
def index():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))
 
    access_token = access_token[0]
    print(access_token)
    
    import urllib.request
    from urllib.request import urlopen
    from urllib.error import URLError
    
    #from urllib2 import Request, urlopen, URLError
 
    headers = {'Authorization': 'OAuth ' + access_token}
    #req = Request('https://www.googleapis.com/oauth2/v1/userinfo',None, headers)

    req = request('https://www.googleapis.com/oauth2/v1/userinfo', None, headers)
    
    try:
        #res = urlopen(req)
        res = urllib.request.urlopen(req)
    except URLError as e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return res.read()
 
    return res.read()
 
 
@app.route('/login')
def login():
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)
 
 
 
@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('index'))
 
 
@google.tokengetter
def get_access_token():
    return session.get('access_token')
 
 
def main():
    app.run()
 
 
if __name__ == '__main__':
    main()
