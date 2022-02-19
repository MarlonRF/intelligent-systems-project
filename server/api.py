from flask import Flask
from flask import request
import os
import pickle
from flask import abort, jsonify


categorias = {0: 'Decoração',
 1: 'Papel e Cia',
 2: 'Outros',
 3: 'Bebê',
 4: 'Lembrancinhas',
 5: 'Bijuterias e Jóias'}

# carrega o caminho do modelo da variável de ambiente "MODEL"
MODEL_PATH = os.environ['MODEL_PATH']
arquivo = open(MODEL_PATH, 'rb')

# modelo classificadorm de texto
mlt = pickle.load(arquivo)
api = Flask(__name__)

@api.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@api.route('/')
def hello():
    return 'Hello, there!'

@api.route("/hello/<nome>", methods=["GET"])
def hello2(nome):
    return {"mensagem":f"Hello, {nome}"}

@api.route("/bye", methods=["POST"])
def bye():
    corpo = request.json
    if not "titulo" in corpo:
        abort(400, description="Não contém titulo")

    texto = request.json['titulo']
    resultado = mlt.predict([texto])
    resultado = categorias[resultado[0]]
    return {'categoria':f"{resultado}"}
   

# main driver function
if __name__ == '__main__':
  
    api.run(debug=True,host='0.0.0.0')