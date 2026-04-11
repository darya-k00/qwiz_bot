import redis

r = redis.Redis(
 host='redis-10994.c13.us-east-1-3.ec2.cloud.redislabs.com',
 port=10994,
 decode_responses=True,
 username="default",
 password="AoMovJVGS14SW7mG7TxIuChwidoqVs7v",
)

try:
    r.ping()
    print("Успешное подключение к Redis")
except redis.exceptions.ConnectionError:
    print("Не удалось подключиться к Redis")
