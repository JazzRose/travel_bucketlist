from db.run_sql import run_sql
from models.city import City
import repositories.location_repository as location_repository

def save(city):
    sql = "INSERT INTO cities (name,info,location_id) VALUES (%s,%s,%s) RETURNING id"
    values = [city.name, city.info, city.location.id]
    results  = run_sql(sql,values)
    city.id = results[0]['id']
    return city
    
def select_all():
    city_list= []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for result in results:
        location = location_repository.select(result["location_id"])
        city = City(result["name"], result["info"],location, result["id"])
        city_list.append(city)
    return city_list

def select(id):
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    location = location_repository.select(result["location_id"])
    city = City(result["name"], location, result["id"])
    return city
