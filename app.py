from flask import Flask, render_template, request, redirect, url_for
import os #Vai ser útil para a criação de pastas a serem adicionadas como upload (para as imagens)
import pymysql #Importa a biblioteca do pymysql (explicação e pesquisa completa no readme)
from werkzeug.utils import secure_filename #É pra conseguir manipular e 

app = Flask(__name__)

# Configurações do MySQL
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'to_do'  # Banco de dados para tarefas

# Pasta de upload
UPLOAD_FOLDER = 'static/uploads/tarefas'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db_connection():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tarefas', methods=['GET', 'POST'])
def tarefas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        prioridade = request.form.get('prioridade')
        concluida = 'sim' if request.form.get('concluida') else 'não'

        imagem = request.files.get('imagem')
        if imagem and imagem.filename:
            filename = secure_filename(imagem.filename)
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
            imagem.save(caminho_imagem)
            caminho_relativo = caminho_imagem.replace('static/', '')
        else:
            caminho_relativo = ''

        cursor.execute("""
            INSERT INTO tarefas (nome, descricao, prioridade, concluida, imagem)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome, descricao, prioridade, concluida, caminho_relativo))
        conn.commit()
        return redirect(url_for('tarefas'))

    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return render_template('tarefas.html', tarefas=tarefas)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        prioridade = request.form.get('prioridade')
        concluida = 'sim' if request.form.get('concluida') else 'não'

        imagem = request.files.get('imagem')
        if imagem and imagem.filename:
            filename = secure_filename(imagem.filename)
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
            imagem.save(caminho_imagem)
            caminho_relativo = caminho_imagem.replace('static/', '')
        else:
            cursor.execute("SELECT imagem FROM tarefas WHERE id = %s", (id,))
            tarefa = cursor.fetchone()
            caminho_relativo = tarefa['imagem']

        cursor.execute("""
            UPDATE tarefas
            SET nome = %s, descricao = %s, prioridade = %s, concluida = %s, imagem = %s
            WHERE id = %s
        """, (nome, descricao, prioridade, concluida, caminho_relativo, id))
        conn.commit()
        conn.close()
        return redirect(url_for('tarefas'))

    cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id,))
    tarefa = cursor.fetchone()
    conn.close()
    return render_template('editar.html', tarefa=tarefa)


@app.route('/deletar/<int:id>', methods=['GET', 'POST'])
def deletar(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id,))
        tarefa = cursor.fetchone()
        conn.close()
        return render_template('confirmar_deletar.html', tarefa=tarefa)

    elif request.method == 'POST':
        cursor.execute("DELETE FROM tarefas WHERE id = %s", (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('tarefas'))

if __name__ == '__main__':
    app.run(debug=True)
