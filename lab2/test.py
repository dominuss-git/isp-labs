from serilizesClass.Json import Json as json

class my:
  b = [1, 2, 3 ,3, 2, 4]
  c = "hello"

def func(a, b):
  c = a + b
  print("hello", c)

def kek(a, b):
  return(a * b)

def to_json(py_obj):
  return {'__class__':'bytes',
          '__value__': list(py_obj)}


class my:
  arr = [1, 2, "3"]
  d = {
  	"a" : {"c": 1, "d": 3, "d": True},
  	"b" : 2 
  }
  b = False
  st = {1, 2, "kirill", 4, 4}
  s = "hello"
  t = (1, 2, "hi",None, ("hello", "blyatt", kek), {1, 2, 3, 3}, [5, 5, 5, {"a" : 1, "b" : 2}])

Json = json() 

a = my().t

a = Json.dumps(a)
print(a)

a = (Json.loads(a)[0][1])

print(a)


# print(a)
