from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/<string:pagename>/')
def render_static(pagename):
    return render_template('%s.html' % pagename)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
