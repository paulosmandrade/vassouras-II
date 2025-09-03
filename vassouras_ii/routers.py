from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

from vassouras_ii.database import get_session
from vassouras_ii.login import verifica_acesso
from vassouras_ii.models import Usuarios

login_manager = LoginManager()

bp = Blueprint(
    'vassouras_ii',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@login_manager.user_loader
def load_user(user_id):
    """Carrega usuário pela sessão"""
    with next(get_session()) as session:
        return session.get(Usuarios, int(user_id))


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')

        status, usuario = verifica_acesso({'email': email, 'password': senha})

        if status:
            login_user(usuario)

            flash(f'Seja bem vindo {usuario.username}!', 'success')

            return redirect(url_for('vassouras_ii.home'))
        else:
            flash('Usuário ou senha inválidas!', 'warning')

    return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('vassouras_ii.login'))


@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')
