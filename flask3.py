from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Index!"
 
@app.route("/blogs")
def hello():
    return "Blogs!"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    app.run()
