#pip install flask
#export FLASK_APP=main.py
#flask run
#para habilitar el modo prueba
#export FLASK_DEBUG=1
from flask import Flask,request,make_response,redirect
from flask.templating import render_template

app = Flask(__name__)

todos = ['GITHUB','PYTHON DESDE CERO','DESARROLLO DE SISTEMAS CON FLASK']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.route('/bs')
def bs():
    return render_template('bs.html')

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':todos,
    }
    return render_template('hello.html',**context)

if __name__ == '__main__':
    app.run(debug = True,port=5000)