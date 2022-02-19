from flask import Flask
from flask import request
import os
import pickle
from flask import abort, jsonify

# Dicionário com os para converter o resultado numérico em string
categorias = {0: 'Decoração',
 1: 'Papel e Cia',
 2: 'Outros',
 3: 'Bebê',
 4: 'Lembrancinhas',
 5: 'Bijuterias e Jóias'}

# carrega o caminho do modelo da variável de ambiente "MODEL_PATH"
MODEL_PATH = os.environ['MODEL_PATH']
arquivo = open(MODEL_PATH, 'rb')

# modelo classificadorm de texto
mlt = pickle.load(arquivo)
api = Flask(__name__)

#Lida com o erro 400
@api.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400

# Home  - Exibe mensagem de saudação da API
@api.route('/')
def hello():
    return 'Hello, there!'

# Recebe JSON com o texto e devolve outro com a categoria predita
@api.route("/bye", methods=["POST"])
def bye():
    corpo = request.json
    # testa se o titulo está no JSON
    if not "titulo" in corpo:
        abort(400, description="Não contém titulo")
    # Se o titulo está no corpo do JSON, executa o modelo
    texto = request.json['titulo']
    resultado = mlt.predict([texto])
    #converte o resultado númerico no nome da categoria
    resultado = categorias[resultado[0]]
    return {'categoria':f"{resultado}"}
   

# função principal
if __name__ == '__main__':
  
    api.run(debug=True,host='0.0.0.0')