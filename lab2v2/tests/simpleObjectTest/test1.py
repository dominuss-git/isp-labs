#!/usr/bin/python3

import sys
sys.path.append('../converter')
# sys.path.append('../../converter')
from createParser.createParcer import CreateSerializator, CreateDeserializator

def Check(test_name, resoult, answer):
  if resoult == answer:
    print(f"   {test_name} ----- ", resoult, answer, '\n' , "PASSED", '\n')
  else:
    print(f"   {test_name} ----- ", resoult, answer, ' -- ' , "FAILED")
    exit()


serializer = CreateSerializator()
deserializer = CreateDeserializator()

print("JSON simple object test with normilize")
try:
  test = None
  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("NoneType", test, d)

  test = False
  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("bool", test, d)

  test = .23423
  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("float", test, d)

  test = 12
  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("int", test, d)

  test = "hello"
  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("str", test, d)

  test = [1, "hello", True, None, 1.24, .23423]
  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("list", test, d)

  test = {1, "hello", True, None, 1.24, .23423}
  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("set", test, d)

  test = (1, "hello", True, None, 1.24, .23423)

  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("tuple", test, d)

  test = {"a" : 1, "b": "hello", "1" : True, "c": None,"f": 1.24,"f2": .23423}

  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("dict", test, d)

  test = Check

  a = serializer.serialize(test, format="JSON")
  d = deserializer.deserialize(a, format="JSON", normalize=True)

  Check("function", Check, d)
except:
  print("FAILED")
  exit()

print('PASSED\n')

