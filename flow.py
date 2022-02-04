from oauth2client.client import OAuth2WebServerFlow

def dump_obj(obj):  
  for attr in dir(obj):
    print (attr)
    #print(getattr(obj, attr))


flow = OAuth2WebServerFlow('secrets/client_secrets_google.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://example.com/auth_return')

print(flow.__dict__)
print(flow.__dict__['client_id'])
#dump_obj(flow.__dict__)

#dump_obj(flow)

