import redis

r = redis.Redis(host = 'localhost', port = 6379, db = 0)

try:
    if r.ping():
        print('Connected to Redis!')
except redis.ConnectionError:
    print('Failed to connect to Redis.')


r.set('my_key', 'Hello, Redis!')

value = r.get('my_key')

print(f'The value extracted fropm Redis is: {value.decode()}')