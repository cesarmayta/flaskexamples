from flask import Flask
from flask import request

app= Flask(__name__)

@app.route('/')
def index():
    return '<h1>HOLA MUNDO FLASK</h1>'

@app.route('/suma')
def suma():
    n1 = request.args.get('n1','ingrese un valor de n1')
    n2 = request.args.get('n2','ingrese un valor de n2')
    r = int(n1) + int(n2)
    return 'la suma de {} + {} es {}'.format(n1,n2,r)

@app.route('/params/')
@app.route('/params/<name>/')
def params(name = "ingresar nombre"):
    return 'El parametro es: {}'.format(name)

@app.route('/calc')
def calculadora():
    form = "<form action='ope' method='POST'>"
    form += "<input type='text' name='n1'/></br>"
    form += "<input type='text' name='n2'/>"
    form += "<input type='submit' value='sumar'/>"
    form += "</form>"
    return form

@app.route('/ope',methods=['POST'])
def operacion():
    if request.method == 'POST':
        n1 = request.form['n1']
        n2 = request.form['n2']
        suma = int(n1) + int(n2)
        return 'la suma es {}'.format(suma)

if __name__ == '__main__':
    app.run(debug = True,port=5000)