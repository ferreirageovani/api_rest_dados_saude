from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carregando o banco de dados
df = pd.read_csv('datasets//atendimentos.csv')

@app.route('/api/v1/atendimentos', methods=['GET'])
def get_atendimentos():
    data_atendimento = request.args.get('data_atendimento')
    condicao_saude = request.args.get('condicao_saude')
    unidade = request.args.get('unidade')

    result = df

    if data_atendimento:
        result = result[result['data_atendimento'] == data_atendimento]
    if condicao_saude:
        result = result[result['condicao_saude'] == condicao_saude]
    if unidade:
        result = result[result['unidade'] == unidade]

    return jsonify(result.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=8001)
