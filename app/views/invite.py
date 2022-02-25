from flask import Blueprint
from flask import render_template
from flask import request


bp = Blueprint(
    name="invite",
    import_name="invite",
    url_prefix="/"
)
base = "https://discord.com"
client_id = 704683198164238446
default_permission = 277025769536
scope = ["applications.commands", "bot"]


@bp.route("/invite", methods=['GET'])
def invite():
    permission = request.args.get("permission", default=default_permission, type=int)
    return render_template(
        'pages/invite.html',
        base=base,
        client_id=client_id,
        scope=scope,
        permission=permission
    )
