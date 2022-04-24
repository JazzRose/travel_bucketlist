from flask import Blueprint, Flask, redirect, render_template,request

from models.location import Location
from models.city import City

import repositories.location_repository as location_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

# CITIES LIST

@cities_blueprint.route("/cities")
def cities():
    city_list = city_repository.select_all()
    return render_template("cities/index.html", city_list = city_list)

# NEW CITY

@cities_blueprint.route("/cities/new")
def new_city():
    return render_template("cities/new.html")

# NEW CITY SUBMIT

@cities_blueprint.route("/cities", methods = ['POST'])
def create_city():
    name = request.form["name"]
    info = request.form["info"]
    location_id = request.form["location_id"]
    location = location_repository.select(location_id)
    new_city= City(name,info,location)
    location_repository.save(new_city)
    return redirect("/cities")

# # EDIT LOCATION

# @locations_blueprint.route("/locations/<id>/edit")
# def edit_location(id):
#     location = location_repository.select(id)
#     return render_template("/locations/edit.html", location = location)

# # SUBMIT EDITED LOCATION

# @locations_blueprint.route("/locations/<id>",methods = ['POST'])
# def update_location(id):
#     name = request.form["name"]
#     type = request.form["type"]
#     info = request.form["info"]
#     visited = False
#     location = Location(name,type,info,visited, id)
#     location_repository.update(location)
#     return redirect("/locations")