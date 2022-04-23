from flask import Blueprint,Flask,redirect,render_template

from models.user  import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users",__name__)

# INDEX
@users_blueprint.route("</username>")
def humans():
    humans = user_repository.select_all()
    return render_template("humans/index.html", users=User)
