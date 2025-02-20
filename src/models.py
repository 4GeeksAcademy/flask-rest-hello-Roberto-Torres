from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):   
    __tablename__ = 'user'

    id_user = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(75), unique=True, nullable=False)
    username = db.Column(db.String(75), unique=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(75), unique=False, nullable=False)
    phone = db.Column(db.String(75), unique=True, nullable=True)
    favorite_people = db.relationship('Favorite_People', backref= 'user')
    favorite_vehicles = db.relationship('Favorite_Vehicles', backref= 'user')
    favorite_planets = db.relationship('Favorite_Planets', backref= 'user')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id_user,
            "email": self.email,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
        }

class People(db.Model):
    __tablename__ = 'people'

    id_people = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    birth_year = db.Column(db.String(25), unique=False, nullable=True)
    gender = db.Column(db.String(15), unique=False, nullable=True)
    height = db.Column(db.String(25), unique=False, nullable=True)
    mass = db.Column(db.String(15), unique=False, nullable=True)
    eye_color = db.Column(db.String(10), unique=False, nullable=True) 
    hair_color = db.Column(db.String(25), unique=False, nullable=True)
    skin_color = db.Column(db.String(25), unique=False, nullable=True) 
    homeworld = db.Column(db.String(250), unique=False, nullable=True) 
    created = db.Column(db.String(100), unique=False, nullable=True) 
    edited = db.Column(db.String(100), unique=False, nullable=True) 
    url = db.Column(db.String(500), unique=True, nullable=True)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id_people,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "homeworld": self.homeworld,
            "created": self.created,
            "edited": self.edited,
            "url": self.url,
        }

class Vehicles(db.Model):
    __tablename__ ='vehicles'

    id_vehicles = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    max_atmosphering_speed = db.Column(db.String(25), unique=False, nullable=True)
    crew = db.Column(db.String(25), unique=False, nullable=True)
    model = db.Column(db.String(75), unique=True, nullable=True)
    vehicle_class = db.Column(db.String(50), unique=False, nullable=True)
    cargo_capacity = db.Column(db.String(75), unique=False, nullable=True)
    consumables = db.Column(db.String(50), unique=False, nullable=True)
    cost_in_credits = db.Column(db.String(50), unique=False, nullable=True)
    length = db.Column(db.String(25), unique=False, nullable=True)
    manufacturer = db.Column(db.String(100), unique=False, nullable=True)
    passengers = db.Column(db.String(25), unique=False, nullable=True)
    created = db.Column(db.String(100), unique=False, nullable=True)
    edited = db.Column(db.String(100), unique=False, nullable=True)
    url = db.Column(db.String(500), unique=True, nullable=True)

    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id_vehicles,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "created": self.created,
            "crew": self.crew,
            "edited": self.edited,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "model": self.model,
            "name": self.name,
            "passengers": self.passengers,
            "url": self.url,
            "vehicle_class": self.vehicle_class,
        }
    
class Planets(db.Model):
    __tablename__ = 'planets'

    id_planets = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    population = db.Column(db.String(25), unique=False, nullable=True)
    climate = db.Column(db.String(25), unique=False, nullable=True)
    diameter = db.Column(db.String(25), unique=False, nullable=True)
    gravity = db.Column(db.String(15), unique=False, nullable=True)
    orbital_period = db.Column(db.String(25), unique=False, nullable=True)
    rotation_period = db.Column(db.String(25), unique=False, nullable=True)
    surface_water = db.Column(db.String(25), unique=False, nullable=True)
    terrain = db.Column(db.String(25), unique=False, nullable=True)
    created = db.Column(db.String(75), unique=False, nullable=True)
    edited = db.Column(db.String(75), unique=False, nullable=True)
    url = db.Column(db.String(500), unique=True, nullable=True)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id_planets,
            "climate": self.climate,
            "created": self.created,
            "diameter": self.diameter,
            "edited": self.edited,
            "gravity": self.gravity,
            "name": self.name,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "url": self.url,
        }
    
# class Favorites(db.Model):
#     __tablename__ = 'favorites'

#     id_favorites = db.Column(db.Integer, primary_key=True)
#     id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
#     id_people = db.Column(db.Integer, db.ForeignKey('people.id_people'), nullable=True)
#     id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id_vehicles'), nullable=True)
#     id_planets = db.Column(db.Integer, db.ForeignKey('planets.id_planets'), nullable=True)

class Favorite_People(db.Model):
    __tablename__ = 'favorite_people'

    id_favorite_people = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    id_people = db.Column(db.Integer, db.ForeignKey('people.id_people'))
    people = db.relationship('People', backref= 'Favorite_People')

    def __repr__(self):
        return '<Favorite_People user_id=%r, people_id=%r>' % (self.id_user, self.id_people)
    
    def serialize(self):
        return {
            "name": self.people.serialize()["name"],
            "id_favorite_people": self.id_favorite_people,
            "id_user": self.id_user,
            "id_people": self.id_people
        }

class Favorite_Vehicles(db.Model):
    __tablename__ = 'favorite_vehicles'

    id_favorite_vehicles = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id_vehicles'))
    vehicles = db.relationship('Vehicles', backref= 'Favorite_Vehicles')

    def __repr__(self):
        return '<Favorite_Vehicles user_id=%r, vehicles_id=%r>' % (self.id_user, self.id_vehicles)
    
    def serialize(self):
        return {
            "name": self.vehicles.serialize()["name"],
            "id_favorite_vehicles": self.id_favorite_vehicles,
            "id_user": self.id_user,
            "id_vehicles": self.id_vehicles
        }


class Favorite_Planets(db.Model):
    __tablename__ = 'favorite_planets'

    id_favorite_planets = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id_planets'))
    planets = db.relationship('Planets', backref= 'Favorite_Planets')

    def __repr__(self):
        return '<Favorite_Planets user_id=%r, planets_id=%r>' % (self.id_user, self.id_planets)
    
    def serialize(self):
        return {
            "name": self.planets.serialize()["name"],
            "id_favorite_planets": self.id_favorite_planets,
            "id_user": self.id_user,
            "id_planets": self.id_planets
        }

