from flask import Blueprint, jsonify

class Planet(): 
    def __init__(self, id, name, description, diameter_km):
        self.id = id
        self.name = name
        self.description = description
        self.diameter_km = diameter_km

planets = [
    Planet(1, "Mercury", "Smallest planet in solar system", 4880), 
    Planet(2, "Venus", "Brightest natural object in Earth's sky besides moon", 12104), 
    Planet(3, "Earth", "Only astronomical object known to harbor life", 12742),
    Planet(4, "Mars", "Red planet", 6779), 
    Planet(5, "Jupiter", "Largest planet in solar system", 139820), 
    Planet(6, "Saturn", "Second largest planet in solar system", 116460),
    Planet(7, "Uranus", "Ice giant", 50724), 
    Planet(8, "Neptune", "Densest giant planet", 49244)
    ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets(): 
    response = []
    for planet in planets:
        response.append(
            {
                "id": planet.id, 
                "name": planet.name,
                "description": planet.description, 
                "diameter_km": planet.diameter_km
            }
        )
    return jsonify(response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({"Message": f"Planet ID {planet_id} is invalid. ID must be integer"}), 400
    chosen_planet = None
    for planet in planets:
        if planet.id == planet_id:
            chosen_planet = {
                "id": planet.id, 
                "name": planet.name,
                "description": planet.description, 
                "diameter_km": planet.diameter_km
            }
    if chosen_planet is None:
        return jsonify({"Message":f"Planet {planet_id} not found."}), 404
    return jsonify(chosen_planet)
