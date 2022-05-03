from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.planets import Planet 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"Planet {planet_id} not found"}, 404))
    
    return planet

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
    return jsonify(response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    planet = Planet.query.get(planet_id)
    
    return {
        "id": planet.id, 
        "name": planet.name,
        "description": planet.description, 
        "diameter_km": planet.diameter_km
    }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter_km = request_body["diameter_km"]

    db.session.commit()
    return make_response(f"Planet #{planet.id} has been successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} has been successfully deleted")