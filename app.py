app = Flask(__name__)

app.register_blueprint(humans_blueprint)
app.register_blueprint(zombies_blueprint)
app.register_blueprint(zombie_types_blueprint)
app.register_blueprint(bitings_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
