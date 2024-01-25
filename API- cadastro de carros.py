from flask import Flask, jsonify, request

app = Flask(__name__)

carros = [
    {
        'id': 1,
        'modelo': 'honda civic',
        'ano': '2024',
        'marca': 'honda',
        'quilometragem': '30,000',
        'faixa de preço': '150,000,00',
    },
    {
        'id': 2,
        'modelo': 'jeep',
        'ano': '2023',
        'marca': 'renegade',
        'quilometragem': '40,000',
        'faixa de preço': '130,000,00',
    },
    {
        'id': 3,
        'modelo': 'toyota',
        'ano': '2022',
        'marca': 'corolla',
        'quilometragem': '50,000',
        'faixa de preço': '120,000,00',
    },
]
@app.route('/carros',methods=['GET'])
def obter_carros():
    return jsonify(carros)
#consultar carro por(id)
@app.route('/carros/<int:id>',methods=['GET'])
def obter_carro_por_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)
#atualizar informações do carro por id
@app.route('/carros/<int:id>',methods=['PUT'])
def editar_carro_por_id(id):
    carro_alterado = request.get_json()
    for indice,carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carro_alterado)
            return jsonify(carros[indice])
#cadastrar veiculo
@app.route('/carros',methods=['POST'])
def incluir_novo_carro():
    novo_carro = request.get_json()
    carros.append(novo_carro)

    return jsonify(carros)
#excluir veiculo por id
@app.route('/carros/<int:id>',methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            del carro[indice]

    return jsonify(carros)

app.run(port=5000,host='localhost',debug=True)