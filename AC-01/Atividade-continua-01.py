from flask import Flask

app = Flask(__name__)

@app.route('/media/<nota1>/<nota2>')
def calcular_media(nota1, nota2):
    media = (float(nota1) + float(nota2)) / 2
    return f'A média das notas é {media}!'

if __name__ == '__main__':
    app.run(debug=True)
