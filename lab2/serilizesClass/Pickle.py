import pickle

class Pickle:
  def dump(self, obj, fl):
    fields = [field for field in dir(obj) if not field.startswith("__")]
    print(obj, fields, fl, sep="\n")
  def dumps(self, obj):
    fields = [field for field in dir(obj) if not field.startswith("__")]
    print(obj, fields, sep="\n")
  def load(self, fl):
    pass
  def loads(self, string):
    pass
