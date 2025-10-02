import sqlite3
from flask import Flask, render_template, request, redirect

# Inicializa a aplicação Flask
app = Flask(__name__)


# Função para criar o banco de dados e a tabela de usuários, caso não existam
def init_db():
    conn = sqlite3.connect("cadastro.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()


# Rota principal: exibe o formulário de cadastro
@app.route("/")
def home():
    return render_template("index.html")


# Rota para cadastrar um novo usuário via formulário
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]  # Obtém o nome do formulário
    email = request.form["email"]  # Obtém o email do formulário

    # Insere o novo usuário no banco de dados
    conn = sqlite3.connect("cadastro.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()

    # Renderiza a página de sucesso, passando os dados cadastrados
    return render_template("sucesso.html", nome=nome, email=email)


# Rota para exibir a lista de usuários cadastrados
@app.route("/usuarios")
def usuarios():
    conn = sqlite3.connect("cadastro.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")  # Busca todos os usuários
    lista = cursor.fetchall()
    conn.close()
    return render_template("lista.html", usuarios=lista)


# Executa a aplicação Flask e inicializa o banco de dados
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
