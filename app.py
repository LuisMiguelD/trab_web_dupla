import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'banco.db')
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_vencimento DATE,
            prioridade TEXT CHECK(prioridade IN ('Baixa', 'Média', 'Alta')),
            status TEXT DEFAULT 'Pendente' CHECK(status IN ('Pendente', 'Em andamento', 'Concluída'))
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    tarefas = conn.execute('SELECT * FROM tarefas').fetchall()
    conn.close()
    return render_template('index.html', lista_tarefas=tarefas)

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/criar', methods=['POST'])
def criar():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    data_vencimento = request.form.get('data_vencimento')
    prioridade = request.form.get('prioridade')

    if not titulo:
        return "Erro: Título é obrigatório!", 400

    conn = get_db_connection()
    conn.execute('''
        INSERT INTO tarefas (titulo, descricao, data_vencimento, prioridade)
        VALUES (?, ?, ?, ?)
    ''', (titulo, descricao, data_vencimento, prioridade))
    conn.commit()
    conn.close()
    
    return redirect('/')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db_connection()

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        data_vencimento = request.form['data_vencimento']
        prioridade = request.form['prioridade']
        status = request.form['status']

        conn.execute('''
            UPDATE tarefas 
            SET titulo = ?, descricao = ?, data_vencimento = ?, prioridade = ?, status = ?
            WHERE id = ?
        ''', (titulo, descricao, data_vencimento, prioridade, status, id))
        conn.commit()
        conn.close()
        return redirect('/')
    
    else:
        tarefa = conn.execute('SELECT * FROM tarefas WHERE id = ?', (id,)).fetchone()
        conn.close()
        return render_template('editar.html', tarefa=tarefa)

@app.route('/deletar/<int:id>')
def deletar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')