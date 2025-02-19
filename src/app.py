"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Vehicles, Planets, Favorite_People, Favorite_Vehicles, Favorite_Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# PEOPLE GET ROUTES

@app.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    data_people = [people.serialize() for people in people]
    return jsonify(data_people), 200

@app.route('/people/<int:id>', methods=['GET'])
def get_people_from_id(id):
    people = People.query.get(id)
    data_people = people.serialize()
    return jsonify(data_people), 200

# VEHICLE GET ROUTES

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicles.query.all()
    data_vehicles = [vehicles.serialize() for vehicles in vehicles]
    return jsonify(data_vehicles), 200

@app.route('/vehicles/<int:id>', methods=['GET'])
def get_vehicles_from_id(id):
    vehicles = Vehicles.query.get(id)
    data_vehicles = vehicles.serialize()
    return jsonify(data_vehicles), 200

# PLANET GET ROUTES

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    data_planets = [planets.serialize() for planets in planets]
    return jsonify(data_planets), 200

@app.route('/planets/<int:id>', methods=['GET'])
def get_planets_from_id(id):
    planets = People.query.get(id)
    data_planets = planets.serialize()
    return jsonify(data_planets), 200

# USER GET ROUTE

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    data_users = [users.serialize() for users in users]
    return jsonify(data_users), 200

# USER FAVORITES GET ROUTE

@app.route('/users/favorites', methods=['GET'])
def get_favorites_user():
    favorite_people = Favorite_People.query.all()
    favorite_vehicles = Favorite_Vehicles.query.all()
    favorite_planets = Favorite_Planets.query.all()
    data_favorite_people = [favorite_people.serialize() for favorite_people in favorite_people]
    data_favorites_vehicles = [favorite_vehicles.serialize() for favorite_vehicles in favorite_vehicles]
    data_favorites_planets = [favorite_planets.serialize() for favorite_planets in favorite_planets]
    return jsonify(data_favorite_people, data_favorites_vehicles, data_favorites_planets), 200

# USER FAVORITE PLANETS POST ROUTE

@app.route('/user/<int:user_id>/favorite/people/<int:people_id>', methods=['POST'])
def add_people_to_favorites(user_id, people_id):

    exist = Favorite_People.query.filter_by(id_user=user_id, id_people=people_id).first()
    if exist:
        return jsonify({"msg": "This character already exists in favorites"}), 400
    new_favorite_people = Favorite_People(id_user=user_id, id_people=people_id)
    db.session.add(new_favorite_people)
    db.session.commit()
    return jsonify({"msg": "Character added to favorites"})


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
