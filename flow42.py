import flask
import json
from oauth2client.client import OAuth2WebServerFlow
import urllib.request


def logdata(content,op):
  f = open('logfile.txt', op);
  f.write(content)
  f.close()

def dump_obj2(obj, level=0):
   for attr in dir(obj):
      val = getattr(obj, attr)
      if isinstance(val, (int, float, str, unicode, list, dict, set)):
           print (level*' ', val)
      else:
           dump(val, level=level+1)
           
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

app = flask.Flask(__name__)

@app.route('/')
def login():

    flow = OAuth2WebServerFlow(client_id='96319319647-76o10sfifhhthldd6avh8p7l83vplqtq.apps.googleusercontent.com',
                           client_secret='hSA3d2SUN7HqnAkH9oR3joki',
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='http://localhost/callback/google')
   
    '''
    flow = flow_from_clientsecrets('secrets/client_secrets_google.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://localhost/callback/google')
    '''
    
    authorization_url = flow.step1_get_authorize_url()
    r= urllib.request.urlopen(authorization_url)
    #print(type(r))
    #print(r.read())
    c=''
    x=r.getheaders()
    for y,z in x:
      if (y=='x-auto-login'):
        #print(y,z)
        c=z
        break
    print(c)
    print(type(c))
    d=c.split("%252")
    for y in d:
      print(y)
     
    
    
    #print(r.headers)
    #print(r.content)
    #logdata(content.decode("utf-8"), 'w+')

    #flask.session['credentials'] = credentials_to_dict(credentials)
    
      
    return "Heello"

@app.route('/callback')
@app.route('/callback/<provider>')
def oauth_callback(provider):
  
  authorization_response = flask.request.url
  flow.fetch_token(authorization_response=authorization_response)
  credentials = flow.credentials
  print(credentials )
  return "hello"
  
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
