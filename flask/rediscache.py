from flask_caching import Cache

config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '172.20.253.185',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_URL': 'redis://172.20.253.185:6379/0',
    'CACHE_REDIS_PASSWORD': 'arbaz',
    'CACHE_DEFAULT_TIMEOUT': 300 
}
cache = Cache(config=config)