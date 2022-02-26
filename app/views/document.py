from flask import Blueprint
from flask import render_template
from flask import request


bp = Blueprint(
    name="document",
    import_name="document",
    url_prefix="/"
)


@bp.route("/privacy", methods=['GET'])
def privacy():
    return render_template(
        'pages/privacy.html'
    )


@bp.route("/term", methods=['GET'])
def term():
    return render_template(
        'pages/term.html'
    )
