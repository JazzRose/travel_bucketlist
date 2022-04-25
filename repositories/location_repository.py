from db.run_sql import run_sql

from models.location import Location
from models.city import City

def save(location):
    sql = "INSERT INTO locations (name,type,info) VALUES (%s, %s, %s) RETURNING id"
    values = [location.name, location.type, location.info]
    results = run_sql(sql,values)
    location.id = results[0]['id']
    return location

def select_all():
    locations = []
    sql = "SELECT * FROM locations"
    results = run_sql(sql)
    for result in results:
        location = Location(result["name"],result["type"], result["info"], result["visited"], result["id"])
        locations.append(location)
    return locations


def select(id):
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    location = Location(result["name"],result["type"], result["info"], result["visited"], result["id"])
    return location

def update(location):
    sql = "UPDATE locations SET (name,type,info) = (%s,%s,%s) WHERE id = %s"
    values = [location.name,location.type,location.info,location.id]
    run_sql(sql,values)

# def select_cities_in_location(id):
#     cities = []
#     sql = "SELECT cities.* FROM cities INNER JOIN locations ON locations.id = cities.location_id WHERE locations.id = %s"
#     values = [id]
#     results = run_sql(sql, values)
#     for result in results:
#         city = City(result["name"], result["info"], result["location"])
#         cities.append(city)
#     return cities
