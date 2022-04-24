from flask import Blueprint,Flask,redirect,render_template,request

from models.location import Location
from models.user import User
from models.city import City
from models.trip import Trip

import repositories.location_repository as location_repository
import repositories.city_repository as city_repository
import repositories.user_repository as user_repository
import repositories.trip_repository as trip_repository

trips_blueprint = Blueprint("trips",__name__)

@trips_blueprint.route("/trips")
def trips():
    trips = trip_repository.select_all()
    return render_template("trips/index.html", trips = trips)

@trips_blueprint.route("trips/new")
def new_trip():
    users = user_repository.select_all()
    cities = city_repository.select_all()
    return render_template ("trips/new.html")

@trips_blueprint.route("/trips", methods = ['POST'])
def create_trip():
    user_id = request.form ["user_id"]
    city_id = request.form["city_id"]
    review = request.form["review"]
    rating = request.form["rating"]
    date = request.form["date"]
    user = user_repository.select(user_id)
    city = city_repository.select(city_id)
    new_trip = Trip(user,city,review,rating,date)
    trip_repository.save(new_trip)
    return redirect("/bitings")