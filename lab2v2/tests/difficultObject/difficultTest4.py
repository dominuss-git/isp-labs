#!/usr/bin/python3

import sys
sys.path.append('../converter')
# sys.path.append('../../converter')
from createParser.createParcer import CreateSerializator, CreateDeserializator

def CheckFields(test_name, resoult, answer):
  if resoult.__init__:
    print(f"  {test_name} -  __init__ ----- ", resoult.__init__, answer.__init__, '\n' , "PASSED", '\n')
  else:
    print(f"  {test_name} -  __init__ ----- ", resoult.__init__, answer.__init__, ' -- ' , "FAILED")
    exit()

  if isinstance(resoult, type):
    resoult = resoult(1, 2)
    answer = answer(1, 2)
  
  if resoult.Hello() == answer.Hello():
    print(f"  {test_name} -  Hello ----- ", resoult.Hello(), answer.Hello(), '\n' , "PASSED", '\n')
  else:
    print(f"  {test_name} -  Hello ----- ", resoult.Hello(), answer.Hello(), ' -- ' , "FAILED")
    exit()

  if resoult.c == answer.c:
    print(f"  {test_name} -  c ----- ", resoult.c, answer.c, '\n' , "PASSED", '\n')
  else:
    print(f"  {test_name} -  c ----- ", resoult.c, answer.c, ' -- ' , "FAILED")
    exit()

def Check(test_name, resoult, answer):
  if resoult == answer:
    print(f"   {test_name} ----- ", resoult, answer, '\n' , "PASSED", '\n')
  else:
    print(f"   {test_name} ----- ", resoult, answer, ' -- ' , "FAILED")
    exit()

class Test:
  def __init__(self, a, b):
    self.count = a
    self.number = b

  def Hello(self):
    return ("hi")

  c = [1, 2, 3, 5, [1, 2, 3, {"dsf", "sdf"}]]

serializer = CreateSerializator()
deserializer = CreateDeserializator()

print("PICKLE difficult test")
try:
  test = {"a" : [1, 3,5,3223, "None"], "b" : {1, 2, 3}, "c" : {"q" : [1, 2, 3], "a": True} }
  a = serializer.serialize(test, format="PICKLE")
  d = deserializer.deserialize(a, format="PICKLE", normalize=True)

  Check("test1", {"a" : [1, 3,5,3223, "None"], "b" : {1, 2, 3}, "c" : {"q" : [1, 2, 3], "a": True}}, d)

  test = {"a" : [1, None, [1, 2, 3, 4]], "c" : [1, 2, 3, (1, 2, 3, 4)] }
  a = serializer.serialize(test, format="PICKLE")
  d = deserializer.deserialize(a, format="PICKLE", normalize=True)   

  Check("test2", {"a" : [1, None, [1, 2, 3, 4]], "c" : [1, 2, 3, (1, 2, 3, 4)] }, d)

  test = [1, 2, 3, 4, [1, 6, True, None, {1, 2, 3, 3}, [1, 2, "hello", (1, 2, 3, 4)]]]
  a = serializer.serialize(test, format="PICKLE")
  d = deserializer.deserialize(a, format="PICKLE", normalize=True)     
  Check("test3", [1, 2, 3, 4, [1, 6, True, None, {1, 2, 3, 3}, [1, 2, "hello", (1, 2, 3, 4)]]], d)

  test = Test
  a = serializer.serialize(test, format="PICKLE")
  d = deserializer.deserialize(a, format="PICKLE", normalize=True)     
  # Check("test4", test, d)
  CheckFields("test4-class-fields-test", Test, d)
except:
  print("FAILED")
  exit()

print('PASSED \n')