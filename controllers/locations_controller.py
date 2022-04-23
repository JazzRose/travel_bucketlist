from flask import Blueprint, Flask, redirect, render_template,request

from models.location import Location
from models.city import City

import repositories.location_repository as location_repository
import repositories.city_repository as city_repository

locations_blueprint = Blueprint("locations", __name__)

# New

@locations_blueprint.route("/locations")
def locations ():
    locations = location_repository.select_all()
    return render_template("locations/index.html", locations = locations)