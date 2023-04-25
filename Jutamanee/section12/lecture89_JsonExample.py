import json
def readJson():
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)

    print(y["name"])
readJson()

def writeJson():
# a Python object (dict):
    x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}# convert into JSON:
    y = json.dumps(x)
# the result is a JSON string:
    print(y)
writeJson()