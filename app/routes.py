from app import app
from flask import render_template

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
    return render_template('cadastro.html', titulo = "cadastro")

@app.route("/login")
def login():
    return render_template('login.html', titulo = "login")

