import json


def readJson():
    # some JSON:
    x = '{ "name":"Paradorn", "age":30, "city":"Rayong"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["name"])


def writeJson():
    # a Python object (dict):

    x = {
        "name": "Paradorn",
        "age": 30,
        "city": "Rayong"
    }

    # convert into JSON:
    jsonString = json.dumps(x)
    jsonFile = open("paradorn.Json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    # the result is a JSON string:
    print(jsonString)


readJson()
writeJson()
