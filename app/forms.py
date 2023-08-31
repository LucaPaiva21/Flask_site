from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired

class Cadastro(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    nascimento = DateField('data-nascimento', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    enviar = SubmitField('enviar')