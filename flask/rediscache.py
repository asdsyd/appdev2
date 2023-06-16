from flask_caching import Cache

config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_URL': 'redis://localhost:6379/0',
    'CACHE_REDIS_PASSWORD': 'arbaz',
    'CACHE_DEFAULT_TIMEOUT': 300 
}
cache = Cache(config=config)