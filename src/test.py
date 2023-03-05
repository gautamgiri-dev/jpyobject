import jpyobject
import json

d = {
    "name": "gautam",
    "roll": 211552
}

js = json.dumps(d)

print(js)

obj = jpyobject.loads(js)

print(obj)

obj.s = 5

print(obj.to_dict())
