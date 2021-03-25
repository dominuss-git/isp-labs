import pickle

class Pickle:
  def dump(self, obj, file_stream):
    return pickle.dump(obj, file_stream)

  def dumps(self, obj):
    return pickle.dumps(obj)

  def load(self, file_stream):
    return pickle.load(file_stream)

  def loads(self, string):
    return pickle.loads(string)