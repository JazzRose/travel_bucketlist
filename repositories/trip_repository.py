from db.run_sql import run_sql
from models.trip import Trip
from models.city import City
from models.user import User


def save (trip):
    sql = "INSERT INTO trips (user_id,city_id,review,rating,date) VALUES (%s,%s,%s,%s,%s)RETURNING id"
    values = [trip.user.id,trip.city.id,trip.review,trip.rating, trip.date]
    results = run_sql(sql,values)
    trip.id =results[0]['id']
    return trip