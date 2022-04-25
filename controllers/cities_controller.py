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
    locations = location_repository.select_all()
    return render_template("cities/new.html", locations = locations)

# NEW CITY SUBMIT

@cities_blueprint.route("/cities", methods = ['POST'])
def create_city():
    name = request.form["name"]
    info = request.form["info"]
    location_id = request.form["location_id"]
    location = location_repository.select(location_id)
    new_city= City(name,info,location)
    city_repository.save(new_city)
    return redirect("/cities")

# EDIT CITY

@cities_blueprint.route("/cities/<id>/edit")
def edit_city(id):
    city = city_repository.select(id)
    locations = location_repository.select_all()
    return render_template("/cities/edit.html", city = city, locations = locations)

# SUBMIT EDITED CITY

@cities_blueprint.route("/cities/<id>",methods = ['POST'])
def update_city(id):
    name = request.form["name"]
    info = request.form["info"]
    location_id = request.form["location_id"]
    location = location_repository.select(location_id)
    city = City(name,info,location,id)
    city_repository.update(city)
    return redirect("/cities")