from fastapi import FastAPI
from pydantic import BaseModel
import redis, sqlite3, json, hashlib
app = FastAPI()
redis_client = redis.Redis(host = 'localhost', port = 6379, db = 0)

#establish database connection
def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row # Try to understand what this is doing, it is important for the result to be a dictionary
    return conn

# setup the database
def init_db():
    conn = get_db_connection() 

    # after connection we need to create a cursor
    # cursor is used to do opeartion in the database

    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER)
    """)

    cursor.execute("""
INSERT INTO users(id, name, age) VALUES (1, 'Michael', 30)""")

    cursor.execute("""
INSERT INTO users(id, name, age) VALUES (2, 'Sarah', 25)
""")

    cursor.execute("""
INSERT INTO users(id, name, age) VALUES (3, 'John', 35)""")

    conn.commit()

    conn.close()

init_db()


class UserQuery(BaseModel):
    user_id :int



def make_cache_key(user_id: int):
    raw = f"user: {user_id}"
    return hashlib.sha256(raw.encode()).hexdigest() # understand what does cache key do


@app.post("/get_user")
async def get_user(user_query: UserQuery):
    key = make_cache_key(user_query.user_id)
    cached_data = redis_client.get(key)

    if cached_data:
        print('Serving from Redis cache')
        return json.load(cached_data)
    else:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
SELECT * FROM users WHERE id = ?""", (user_query.user_id))

        row = cursor. fetchone() # take out the one result

        conn.close()

        if row is None:
            return {"error": "User not found"}
        else:
            result = dict(row)
            redis_client.set(key, json.dumps(result), ex = 3600) # cache for 1 hour
            print("fetch results from db")
            return result