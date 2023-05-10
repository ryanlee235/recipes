from flask import Blueprint, render_template, request

bp = Blueprint("view", __name__, static_folder="static", template_folder='templates')

@bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")