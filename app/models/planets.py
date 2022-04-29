from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    diameter_km = db.Column(db.Integer)



# class Planet(): 
#     def __init__(self, id, name, description, diameter_km):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.diameter_km = diameter_km

# planets = [
#     Planet(1, "Mercury", "Smallest planet in solar system", 4880), 
#     Planet(2, "Venus", "Brightest natural object in Earth's sky besides moon", 12104), 
#     Planet(3, "Earth", "Only astronomical object known to harbor life", 12742),
#     Planet(4, "Mars", "Red planet", 6779), 
#     Planet(5, "Jupiter", "Largest planet in solar system", 139820), 
#     Planet(6, "Saturn", "Second largest planet in solar system", 116460),
#     Planet(7, "Uranus", "Ice giant", 50724), 
#     Planet(8, "Neptune", "Densest giant planet", 49244)
# ]