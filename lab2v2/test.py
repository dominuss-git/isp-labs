from createParser.createParcer import CreateSerializator, CreateDeserializator

class Some:
  d = "troll"
  def Hello():
    print("hi")

class Method(Some):
  a = "hi"
  b = "oi"
  c = [1, 2, 3]
  def df():
    print(d)

def func(a, b):
  retrun (a + b)

s = CreateSerializator()
b = [1, 2, 3, 4]
a = { "a": 1, "b": 2, "c": b }
a2 = { "a": 1, "b": 2, "c" : a}
f = {1, 2, 3, 4}
c = [True, False, f, a]
r2 = (1, 2, 3, (1, 2, 3))

string = "hi"

k = Method()

r = k
# s.serialize(b, format='JSON', file_path='json.json')

# s.serialize(c, format='JSON', file_path='json.json')

d = CreateDeserializator()

# q = d.deserialize('json.json', format='JSON', file_mode=True, normalize=True)

# s.serialize(r, format='YAML', file_path='yaml.yaml')
s.serialize(a2, format='TOML', file_path='toml.toml')

q = d.deserialize('toml.toml', format='TOML', file_mode=True, normalize=True)

# print(q.d)

print(type(q), q, "here")