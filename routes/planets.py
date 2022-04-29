from flask import Blueprint, jsonify, request 
from app import db
from app.models.planets import Planet 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"], 
        description=request_body["description"],
        diameter_km=request_body["diameter_km"]
    )
    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201


@planets_bp.route("", methods=["GET"])
def get_all_planets(): 
    response = []
    planets = Planet.query.all()
    for planet in planets:
        response.append(
            {
                "id": planet.id, 
                "name": planet.name,
                "description": planet.description, 
                "diameter_km": planet.diameter_km
            }
        )
    # pdb.set_trace()
    return response

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    # create helper function to validate planets
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({"Message": f"Planet ID {planet_id} is invalid. ID must be integer"}), 400

    chosen_planet = None
    planets = Planet.query.all()
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
