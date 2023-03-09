# Importando o módulo Flask para criar um aplicativo web
from flask import Flask, request, render_template

# Criando a instância do aplicativo
app = Flask(__name__)

# Rota principal com tratamento caso as notas ainda não tenham sido informadas pelo usuário
@app.route('/index', methods=['GET', 'POST'])
def index():
    resultado = None
    media = None
    nota1 = request.args.get('nota1')
    nota2 = request.args.get('nota2')

    # Verifica se as notas foram preenchidas pelo usuário
    if nota1 and nota2:
        nota1 = float(nota1)
        nota2 = float(nota2)

        media = (nota1 + nota2) / 2

        # Verificando se o aluno foi aprovado, reprovado ou ficou em DP
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

    return render_template('index.html', media=media, resultado=resultado)

# Iniciando o servidor da aplicação se esse módulo for o principal
if __name__ == '__main__':
    app.run(debug=True)
