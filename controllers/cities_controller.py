from flask import Blueprint, Flask, redirect, render_template,request

from models.location import Location
from models.city import City
from models.user import User
from models.trip import Trip

import repositories.location_repository as location_repository
import repositories.city_repository as city_repository
import repositories.user_repository as user_repository
import repositories.trip_repository as trip_repository

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

# REVIEW CITY

@cities_blueprint.route("/cities/<id>/trip")
def review_city(id):
    city = city_repository.select(id)
    users = user_repository.select_all()
    return render_template("/cities/trip.html", city = city, users= users)

@cities_blueprint.route("/cities/trip", methods = ['POST'])
def submit_review():
    user_id = request.form ["user_id"]
    city_id = request.form[("city_id")]
    review = request.form["review"]
    rating = request.form["rating"]
    date = request.form["date"]
    user = user_repository.select(user_id)
    city = city_repository.select(city_id)
    trip = Trip(user,city,review,rating,date)
    trip_repository.save(trip)
    return redirect("/trips")

# DELETE CITY

@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_location(id):
    city_repository.delete(id)
    return redirect("/cities")