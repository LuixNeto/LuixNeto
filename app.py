from flask import Flask, jsonify, request
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)

app = Flask(__name__)

produtos = [
    {
        'codigo': 1,
        'descricao': 'Teclado',
        'preco': '10',
        'categoria': 'Eletronicos',

    },
]

# @app.route('/livros',methods=['GET'])
# def obter_livros():
#     return jsonify(livros)

# @app.route('/livros/<int:id>',methods=['GET'])
# def obter_livro_por_id(id):
#     for livro in livros:
#         if livro.get('id') == id:
#             return jsonify(livro)

# @app.route('/livros/<int:id>',methods=['PUT'])
# def editar_livro_por_id(id):
#     livro_alterado = request.get_json()
#     for indice,livro in enumerate(livros):
#       if livro.get('id') == id:
#         livros[indice].update(livro_alterado)
#         return jsonify(livros[indice])
    
@app.route('/produtos',methods=['POST'])
def incluir_novo_produto():
    novo_produto = request.get_json()
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(novo_produto.get('codigo')),str(novo_produto.get('descricao')),str(novo_produto.get('preco')),novo_produto.get('categoria'))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    return "Produto cadastrado com sucesso!"

# @app.route('/livros/<int:id>',methods=['DELETE'])
# def excluir_livro(id):
#     for indice, livro in enumerate(livros):
#         if livro.get('id') == id:
#             del livros[indice]

#     return jsonify(livros)

app.run(port='5000',host='localhost',debug=True)