from app import app

#decorator -> aplicar uma funcao em cima de outra
#definindo uma rota
@app.route("/")
def index():
    return "Hello world!"