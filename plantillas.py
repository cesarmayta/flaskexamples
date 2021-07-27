from flask import Flask
from flask import request
from flask import make_response,redirect,render_template

app = Flask(__name__)

@app.route("/")
def index():
    nombre = request.args.get('name','ingrese un valor de n2')
    return render_template('index.html',name=nombre)
    
    

app.run(debug=True,port=5000)