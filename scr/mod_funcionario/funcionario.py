from flask import Blueprint, render_template
bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' rotas dos formulários '''

@bp_funcionario.route('/', methods=['GET','POST'])
def formListaFuncionario():
    return render_template('formListaFuncionario.html'), 200

@bp_funcionario.route('/form-funcionario/', methods=['POST'])
def formFuncionario():
    return render_template('formFuncionario.html'), 200

# '''
# Rota antiga de app...
# @app.route('/funcionario/')
# def formListaFuncionario():
#   # return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
#   return render_template('formListaFuncionario.html'), 200
# '''