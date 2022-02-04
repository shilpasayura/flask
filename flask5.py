from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App!"
 
@app.route("/members/<string:name>/")
def members(name):
    return render_template(
        'name_template1.html',name=name)
 
if __name__ == "__main__":
    # app runs on port 8000 or 80
    app.run(host='0.0.0.0', port=8000)
