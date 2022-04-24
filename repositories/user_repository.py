from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (username, age, interests) VALUES (%s,%s,%s) RETURNING id"
    values = [user.username, user.age, user.interests]
    results  = run_sql(sql,values)
    user.id = results[0]['id']
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for result in results:
        user = User(result["username"], result ["age"], result ["interests"], result ["id"])
        users.append(user)
    return users

def select(id):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    user = User(result["username"], result ["age"], result ["interests"], result ["id"])
    return user
