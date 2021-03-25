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

print("JSON write test")

test = None
serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("NoneType", test, d)

test = False
serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("bool", test, d)

test = .23423
serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("float", test, d)

test = 12
serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("int", test, d)

test = "hello"
serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("str", test, d)

test = [1, "hello", True, None, 1.24, .23423]
serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("list", test, d)

test = {1, "hello", True, None, 1.24, .23423}
serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("set", test, d)

test = (1, "hello", True, None, 1.24, .23423)

serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("tuple", test, d)

test = {"a" : 1, "b": "hello", "1" : True, "c": None,"f": 1.24,"f2": .23423}

serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("dict", test, d)

test = Check

serializer.serialize(test, format="JSON", file_path='/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json')
d = deserializer.deserialize('/home/dominuss/labs/lab2v2/tests/writeToFile/out/testjson.json', format="JSON", normalize=True, file_mode=True)

Check("function", Check, d)

print('PASSED \n')