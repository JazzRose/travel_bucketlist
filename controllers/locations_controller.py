from flask import Blueprint, Flask, redirect, render_template,request

from models.location import Location
from models.city import City

import repositories.location_repository as location_repository
import repositories.city_repository as city_repository

locations_blueprint = Blueprint("locations", __name__)

# LOCATIONS LIST

@locations_blueprint.route("/locations")
def locations():
    locations = location_repository.select_all()
    return render_template("locations/index.html", locations = locations)

# NEW LOCATION

@locations_blueprint.route("/locations/new")
def new_location():
    return render_template("locations/new.html")

# NEW LOCATION SUBMIT

@locations_blueprint.route("/locations", methods = ['POST'])
def create_location():
    name = request.form["name"]
    type = request.form["type"]
    info = request.form["info"]
    new_location = Location(name,type,info)
    location_repository.save(new_location)
    return redirect("/locations")

# EDIT LOCATION

@locations_blueprint.route("/locations/<id>/edit")
def edit_location(id):
    location = location_repository.select(id)
    return render_template("/locations/edit.html", location = location)

# SUBMIT EDITED LOCATION

@locations_blueprint.route("/locations/<id>",methods = ['POST'])
def update_location(id):
    name = request.form["name"]
    type = request.form["type"]
    info = request.form["info"]
    visited = False
    location = Location(name,type,info,visited, id)
    location_repository.update(location)
    return redirect("/locations")

# @locations_blueprint.route("/locations<id>/cities")
# def cities_in_location(id):
#     cities = location_repository.select_cities_in_location(id)
#     return render_template("/locations/cities.html", cities = cities)
