import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    password="init1234"
)
print("~~~~~~~~~~~ Connected ~~~~~~~~~~~~\n")
# to set the value in database
# r.set("salary", "10,000")

# to get the value from the database
# value = r.get("country")
# print(value)
