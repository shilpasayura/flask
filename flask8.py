from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
import  urllib.request
 
#tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
#app = Flask(__name__, template_folder=tmpl_dir)
app = Flask(__name__)

def getExchangeRates():
    rates = []
    url='http://data.fixer.io/api/latest?access_key=8bd5ee6558c7ab5865178a62edbeceb6'
    response = urllib.request.urlopen(url)
    data = response.read()
    rdata = json.loads(data, parse_float=float)

    rates.append( rdata['rates']['USD'] )
    rates.append( rdata['rates']['GBP'] )
    rates.append( rdata['rates']['EUR'] )
    rates.append( rdata['rates']['AUD'] )
    rates.append( rdata['rates']['SGD'] )
    return rates
 
@app.route("/")
def index():
    rates = getExchangeRates()
    return render_template('chart.html',**locals())
@app.route("/hello")
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
