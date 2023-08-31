from app import app
from flask import render_template, request, flash, redirect
from app.forms import Cadastro


@app.route("/")
def index():
    return render_template('index.html', titulo = "Ei Tech")

@app.route("/produtos")
def produtos():
    return render_template('produtos.html', titulo = "produtos")

@app.route("/sobre")
def sobre():
    return render_template('sobre.html', titulo = "sobre")

@app.route("/cadastro")
def cadastro():
    cadastro = Cadastro()
    nome = cadastro.nome.data
    email = cadastro.email.data
    nacimento = cadastro.nascimento.data
    senha = cadastro.senha.data
    if cadastro.validate_on_submit():
        flash("Dados enviados com sucesso")
        redirect('cadastro.html')
    return render_template('cadastro.html', titulo = "cadastro", cadastro = cadastro)

@app.route("/login")
def login():
    return render_template('login.html', titulo = "login")


@app.route("/dados", methods=['GET', 'POST'])
def dados(): 
    nome = request.args.get('nome')
    email = request.args.get('email')
    nascimento = request.args.get('data-nascimento')
    senha = request.args.get('senha')
    if len(senha) != 0:
        flash("Campo senha vazio")
        redirect('cadastro.html')
    return f"Nome: {nome}\nEmail: {email}\nNascimento: {nascimento}\nSenha: {senha}"
