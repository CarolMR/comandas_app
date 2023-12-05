from flask import Blueprint, render_template

bp_index = Blueprint('index', __name__, template_folder='templates', url_prefix="/home")

''' rotas dos formulários '''

# @bp_index.route('/', methods=['GET', 'POST'])   
@bp_index.route('/')
def formIndex():    
     return render_template('formIndex.html'), 200

# @bp_index.route('/form-index/', methods=['GET'])
# def formIndex():
#       return render_template('formIndex.html'), 200

# @bp_index.route('/')
# def formIndex():
#      return render_template('formIndex.html'), 200