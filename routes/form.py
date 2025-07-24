from flask import Blueprint, render_template, flash, redirect, url_for, session
from forms import CadastroForm, LoginForm
from models import Usuarios, db
from werkzeug.security import generate_password_hash, check_password_hash

form_route = Blueprint('auth', __name__, url_prefix='/auth')

@form_route.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data
        senha_hash = generate_password_hash(senha)

        usuario_existente = Usuarios.query.filter_by(email = email).first()
        if not usuario_existente:
            usuario = Usuarios(nome = nome, email = email, senha = senha_hash)

            db.session.add(usuario)
            db.session.commit()
            flash('Usuário cadastrado com sucesso!')
            return redirect(url_for('auth.cadastro'))
        
        else:
            flash('Usuário já existente.')
            return redirect(url_for('auth.cadastro'))

    return render_template('cadastro.html', form = form)

@form_route.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        senha = form.senha.data

        usuario_existente = Usuarios.query.filter_by(email = email).first()

        if usuario_existente and check_password_hash(usuario_existente.senha, senha):
            session['usuario_nome'] = usuario_existente.nome
            session['usuario_email'] = usuario_existente.email

            return redirect(url_for('auth.dashboard'))
        else:
            flash ('E-mail ou senha incorretos.')
            return redirect(url_for('auth.login'))

    return render_template('login.html', form = form)

@form_route.route('/logout')
def logout():
    session.pop('usuario_nome', None)
    session.pop('usuario_email', None)
    return redirect(url_for('home.homepage'))

@form_route.route('/dashboard')
def dashboard():
    nome = session.get('usuario_nome')
    email = session.get('usuario_email')

    if not nome or not email:
        flash ('Você precisa estar logado para acessar esta página.')
        return redirect(url_for('auth.login'))

    return render_template('dashboard.html', nome = nome, email = email)    