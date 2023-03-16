from flask import Flask, request

app = Flask(__name__)

@app.route('/media', methods=['GET'])
def calcular_media():
    nota1 = float(request.args.get('nota1'))
    nota2 = float(request.args.get('nota2'))

    media = (nota1 + nota2) / 2
    
    return f'A média das notas {nota1:.2f} e {nota2:.2f} é: {media:.2f}'

if __name__ == '__main__':
    app.run(debug=True)
