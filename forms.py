from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(message='Campo do nome está vazio.')])
    email = StringField('E-mail', validators=[DataRequired(message='Campo do e-mail está vazio.'),
                                              Email(message='E-mail inválido.')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Preencha o campo com sua senha.'),
                                               Length(min=8, message='A senha precisa ter no mínimo 8 caracteres')])
    conf_senha = PasswordField('Confirmar Senha', validators=[DataRequired(message='Preencha o campo com sua senha.'),
                                                            Length(min=8, message='A senha precisa ter no mínimo 8 caracteres'),
                                                            EqualTo('senha', message='As senhas não coincidem.')])
    enviar = SubmitField('Enviar')
    
class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(message='Preencha com seu e-mail.'),
                                              Email(message='E-mail inválido.')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Preencha o campo com sua senha.'),
                                               Length(min=8, message='A senha precisa ter no mínimo 8 caracteres')])
    enviar = SubmitField('Enviar')