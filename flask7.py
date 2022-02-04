
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_debugtoolbar import DebugToolbarExtension

# App config.

app = Flask(__name__)
app.debug = False
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'gh5641rtf27567ddd441f2b6176a'
toolbar = DebugToolbarExtension(app)

class ReusableForm(Form):
    userid = TextField('User ID:', validators=[validators.required()])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=6, max=15)])
 
 
@app.route("/", methods=['GET', 'POST'])
def index():
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        userid=request.form['userid']
        password=request.form['password']
        print (userid,  password)
 
        if form.validate():
            # Save the comment here.
            flash('Thanks ' + userid)
        else:
            flash('Error: all fields required. ')
 
    return render_template('login.html', form=form)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
