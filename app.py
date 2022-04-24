from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder='templates')

from controllers.locations_controller import locations_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.trips_controller import trips_blueprint

# app.register_blueprint(users_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(locations_blueprint)
app.register_blueprint(trips_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
