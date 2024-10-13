from flask import  render_template, Blueprint


core = Blueprint('core', __name__ , template_folder='templates')

@core.route('/')
def index():
    return render_template(template_name_or_list='core/index.html')

