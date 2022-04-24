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

