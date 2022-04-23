from db.run_sql import run_sql
from models.city import City

def save(city):
    sql = "INSERT INTO cities (name, info) VALUES (%s,%s) RETURNING id"
    values = [city.name, city.info]
    results  = run_sql(sql,values)
    city.id = results[0]['id']
    return city