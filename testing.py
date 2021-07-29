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
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
from flask import flash
import unittest


app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['SECRET_KEY'] = 'SUPER SECRETO'

bootstrap = Bootstrap(app)

todos = ['GITHUB','PYTHON DESDE CERO','DESARROLLO DE SISTEMAS CON FLASK']

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    Submit = SubmitField('Login')

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


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
    session['user_ip'] = user_ip
    #response.set_cookie('user_ip',user_ip)

    return response

@app.route('/hello',methods=['GET','POST'])
def hello():
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = session.get('username')
    
    #creamos un objeto de la clase LoginForm
    login_form = LoginForm()

    context = {
        'user_ip':user_ip,
        'todos':todos,
        'login_form':login_form,
        'username':username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        #if username == 'admin' and password == '12345':
        session['username'] = username

        flash('Acceso Exitoso')

        return redirect(url_for('index'))
    

    return render_template('hello.html',**context)

if __name__ == '__main__':
    app.run(debug = True,port=5000)