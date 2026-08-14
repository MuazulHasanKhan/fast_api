import redis
import json
import hashlib
import httpx
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

class PostRequest(BaseModel):
    post_id: int

def make_cache_key(post_id:int):
    raw = f"external_api:post_{post_id}"

    return hashlib.sha256(raw.encode()).hexdigest()


@app.post('/get_post')
async def get_post(post_request: PostRequest):
    cache_key = make_cache_key(post_request.post_id)

    cached_data = redis_client.get(cache_key)

    if cached_data:
        print("Cache hit")
        return json.loads(cached_data)
    
    print("Calling external api")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{post_request.post_id}")
        if response.status_code != 200:
            return {"error": "Failed to fetch data from external API"}

    post_data = response.json()
    redis_client.set(cache_key, json.dumps(post_data), ex=3600)  # Cache for 1 hour
    print('Fetched and stored in Cache!')
    return post_data


