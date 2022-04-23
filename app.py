from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

from controllers.locations_controller import locations_blueprint

# app.register_blueprint(users_blueprint)
# app.register_blueprint(cities_blueprint)
app.register_blueprint(locations_blueprint)
# app.register_blueprint(trips_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
