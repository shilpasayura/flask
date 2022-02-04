from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# secret key is needed to keep the client-side sessions secure.
# You can generate some random key

app.config['SECRET_KEY'] = b'\x97\xc5\xa0\xa1\xc6EM\xa0\x0e\xc9\xc6gR\xaf\xe2\x1br\xf2K\x84\x8d\xbe\x9f@'
toolbar = DebugToolbarExtension(app)

@app.route('/')
def hello_world():
    return '<body>Hello, Flask!</body>'

if __name__ == '__main__':
    app.run()








