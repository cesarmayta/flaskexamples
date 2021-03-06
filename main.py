#pip install flask
#export FLASK_APP=main.py
#flask run
#para habilitar el modo prueba
#export FLASK_DEBUG=1
from flask import Flask,request,make_response,redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask_bootstrap import Bootstrap
from flask import session
from flask import flash
import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()


todos = ['GITHUB','PYTHON DESDE CERO','DESARROLLO DE SISTEMAS CON FLASK']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    #response.set_cookie('user_ip',user_ip)

    return response

@app.route('/hello',methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    #login_form = LoginForm()
    username = session.get('username')

    
    context = {
        'user_ip':user_ip,
        'todos':todos,
        #'login_form':login_form,
        'username':username
    }

    
    
    return render_template('hello.html',**context)
