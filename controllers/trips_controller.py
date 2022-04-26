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
    top_citys_and_ratings = trip_repository.top_trips()

    top_citys = top_citys_and_ratings[0]
    ratings = top_citys_and_ratings[1]

    return render_template("trips/index.html", trips = trips, top_citys= top_citys, ratings=ratings)

@trips_blueprint.route("/trips/new")
def new_trip():
    users = user_repository.select_all()
    cities = city_repository.select_all()
    return render_template ("trips/new.html", users = users, cities = cities)

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
    return redirect("/trips")

# EDIT TRIP

@trips_blueprint.route("/trips/<id>/edit")
def edit_trip(id):
    trip = trip_repository.select(id)
    cities = city_repository.select_all()
    users = user_repository.select_all()
    return render_template("/trips/edit.html", cities = cities, users = users, trip = trip)

# SUBMIT EDITED TRIP

@trips_blueprint.route("/trips/<id>",methods = ['POST'])
def update_trip(id):
    user_id = request.form ["user_id"]
    city_id = request.form["city_id"]
    review = request.form["review"]
    rating = request.form["rating"]
    date = request.form["date"]
    user = user_repository.select(user_id)
    city = city_repository.select(city_id)
    trip = Trip(user,city,review,rating,date,id)
    trip_repository.update(trip)
    return redirect("/trips")


# DELETE TRIP

@trips_blueprint.route("/trips/<id>/delete", methods=["POST"])
def delete_trip(id):
    trip_repository.delete(id)
    return redirect("/trips")
