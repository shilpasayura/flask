from oauth2client.client import OAuth2WebServerFlow

def dump_obj(obj):  
  for attr in dir(obj):
    print (attr)
    #print(getattr(obj, attr))


flow = OAuth2WebServerFlow('secrets/client_secrets_google.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://example.com/auth_return')
auth_uri = flow.step1_get_authorize_url()

print(auth_uri)


