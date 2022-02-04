# WSGI application
# retrieve its HTTP status line, response headers, and response body as Python objects


from io import BytesIO

def call_application(app, environ):
    status = None
    headers = None
    body = BytesIO()
    
    def start_response(rstatus, rheaders):
        nonlocal status, headers
        status, headers = rstatus, rheaders
        
    app_iter = app(environ, start_response)
    
    try:
        for data in app_iter:
            assert status is not None and headers is not None, \
                "start_response() was not called"
            body.write(data)
    finally:
        if hasattr(app_iter, 'close'):
            app_iter.close()
    return status, headers, body.getvalue()

environ = {...}  # "environ" dict
status, headers, body = call_application(app, environ)
