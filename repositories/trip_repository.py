from db.run_sql import run_sql
from models.trip import Trip
from models.city import City
from models.user import User

import repositories.location_repository as location_repository
import repositories.city_repository as city_repository
import repositories.user_repository as user_repository
import repositories.trip_repository as trip_repository



def save (trip):
    sql = "INSERT INTO trips (user_id,city_id,review,rating,date) VALUES (%s,%s,%s,%s,%s)RETURNING id"
    values = [trip.user.id,trip.city.id,trip.review,trip.rating, trip.date]
    results = run_sql(sql,values)
    trip.id =results[0]['id']
    return trip

def select_all():
    trips = []
    sql = "SELECT * from trips"
    results = run_sql(sql)
    
    for row in results:
        user = user_repository.select(row['user_id'])
        city = city_repository.select(row['city_id'])
        trip = Trip(user,city,row['review'],row['rating'],row['date'],row['id'])
        trips.append(trips)
    return trips

def select (id):
    sql = "SELECT *FROM trips WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    user = user_repository.select(['user_id'])
    city = city_repository.select(['city_id'])
    trip = Trip(user,city,result['review'],result['rating'],result['date'],result['id'])
    return trip

def update(trip):
    sql = "UPDATE trips SET (user_id,city_id,review,rating,date) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [trip.user_id, trip.city_id,trip.review,trip.rating,trip.date]
    run_sql(sql, values)