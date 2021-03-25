import yaml
import pickle
import types
import logging
import inspect
import base64

class Yaml:
  def dump(self, obj, file_stream):
    return yaml.dump(self._prepare(obj), file_stream, indent=2)

  def dumps(self, obj):
    return yaml.dump(self._prepare(obj))

  def load(self, file_stream):
    return yaml.load(file_stream)

  def loads(self, string):
    return yaml.load(string, Loader=yaml.FullLoader)

  def _prepare(self, obj):
    if isinstance(obj, (int, float, int, bool, str)) or \
      obj is None:
      return obj
    elif isinstance(obj, (set, tuple)):
      s_obj = str(base64.b64encode(pickle.dumps(obj)))

      return {
        "__type__" : str(type(obj)),
        "__base64__" : s_obj[2:len(s_obj) - 1],
      }

    elif isinstance(obj, list):
      for index in range(len(obj)):
        obj[index] = self._prepare(obj[index])

      return obj
    
    elif isinstance(obj, types.FunctionType):
      s_obj = str(base64.b64encode(pickle.dumps(obj)))
      source = []
      out = ""

      for char in inspect.getsource(obj):
        if char == '\n':
          source.append(out)
          out = ""
          continue

        out += char        

      return {
        "__type__" : str(type(obj)),
        "__name__" : obj.__name__,
        "__sorce__" : source,
        "__base64__" : s_obj[2:len(s_obj) - 1],
      }

    elif isinstance(obj, dict):
      for key, value in obj.items():
        obj[key] = self._prepare(value)

      return obj

    else:
      # value = dict()
      try:
        # fields = [field for field in dir(obj) if not field.startswith("__")]
        # print(obj)
        s_obj = str(base64.b64encode(pickle.dumps(obj)))

        # print(s_obj)

        if obj.__class__.__name__ == 'type':
          name = obj.__name__ 
        else:
          name = obj.__class__.__name__

        return {
          "__type__" : str(type(obj)),
          "__name__" : name,
          "__base64__" : s_obj[2: len(s_obj) - 1]
        }

      except:
        logging.error(repr(obj) + ' is not yaml serializable')
        exit()

      