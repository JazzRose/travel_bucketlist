from db.run_sql import run_sql

from models.location import Location
from models.city import City

def save(location):
    sql = "INSERT INTO locations (name,type,info) VALUES (%s, %s, %s) RETURNING id"
    values = [location.name, location.type, location.info]
    results = run_sql(sql,values)
    location.id = results[0]['id']
    return location