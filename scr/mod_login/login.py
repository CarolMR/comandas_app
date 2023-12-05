from flask import Blueprint, render_template, request, redirect, url_for, session
from funcoes import Funcoes
from functools import wraps
from flask import jsonify

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")

@bp_login.route('/login', methods=['POST'])
def validaLogin():
    try:
        cpf = request.form['usuario']
        senha = Funcoes.cifraSenha(request.form['senha'])

        session.clear()

        if (cpf == "abc" and senha == Funcoes.cifraSenha('Bolinhas')):
            session['login'] = cpf
            
            return redirect(url_for('index.formIndex'))
        else:
            raise Exception("Falha de Login! Verifique seus dados e tente novamente!")
        

    except Exception as e:
        return redirect(url_for('login.login', msgErro=e.args[0]))
    
@bp_login.route("/logoff", methods=['GET'])
def logoff():
    
    session.pop('login', None)
    
    session.clear()
    
    return redirect(url_for('login.login'))

def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' not in session:

            return redirect(url_for('login.login', msgErro='Usuário não logado!'))
        else:
            return f(*args, **kwargs)
    return decorated_function