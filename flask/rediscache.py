from flask_caching import Cache
from redis import StrictRedis
config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_URL': 'redis://localhost:6379/0',
    'CACHE_DEFAULT_TIMEOUT': 20 
}
cache = Cache(config=config)

redis = StrictRedis("127.0.0.1",6379)

def deletekey(key:str):
    if redis.exists(key):
        redis.delete(key)
