from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

dashboard = Blueprint('controllers', __name__, template_folder='templates')


@dashboard.route('/', methods=['GET'])
def serve_dashboard():
    try:
        return render_template('index.html', title="Title")
    except TemplateNotFound:
        abort(404)
