from flask import Blueprint, render_template, session


home_route = Blueprint('home', __name__)

@home_route.route('/')
def homepage():
    usuario = None
    disabled = False


    if session.get('usuario_nome'):
        usuario = session.get('usuario_nome')
        disabled = True
    else:
        disabled = False

    return render_template('home.html', usuario_nome = usuario, disabled=disabled)