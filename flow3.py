from flask import Flask
from oauth2client.client import OAuth2WebServerFlow

def dump_obj(obj):  
  for attr in dir(obj):
    print (attr)
    #print(getattr(obj, attr))

app = Flask(__name__)

@app.route('/')
def login():
    flow = OAuth2WebServerFlow('secrets/client_secrets_google.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://example.com/auth_return')
    auth_uri = flow.step1_get_authorize_url()
    print(auth_uri)
    return auth_uri



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
