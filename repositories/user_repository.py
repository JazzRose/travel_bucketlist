from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (username, age, interests) VALUES (%s,%s,%s) RETURNING id"
    values = [user.username, user.age, user.interests]
    results  = run_sql(sql,values)
    user.id = results[0]['id']
    return user