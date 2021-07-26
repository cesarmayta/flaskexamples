from flask import Flask
#https://github.com/gmondragon/nazk
#https://github.com/JoseSpx/ApiConsultaSunatRUC
app= Flask(__name__)

@app.route('/')
def index():
    return '<h1>HOLA MUNDO FLASK</h1>'

app.run()