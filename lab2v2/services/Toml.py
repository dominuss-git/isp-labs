import toml
import pickle
import types
import logging
import inspect
import base64

class Toml:
  def dump(self, obj, file_stream):
    # args = inspect.getargspec(self.dump).arg
    # line = inspect.getouterframes(inspect.currentframe())[1][4][0]
    # actual_args = map(str.strip, line[line.index('(') + 1: line.index(')')].split(','))
    # names = []

    # try:
    #   for key, val in zip(args, actual_args):
    #     names.append(val)
    #     # break

    # except:
    #   logging.error(obj + " can't have name")
      

    return toml.dump(self._prepare(obj, True), file_stream)

  def dumps(self, obj):
    # args = inspect.getargspec(self._prepare).args
    # line = inspect.getouterframes(inspect.currentframe())[1][4][0]
    # actual_args = map(str.strip, line[line.index('(') + 1: line.index(')')].split(','))
    # names = []

    # try:
    #   for val in zip(args, actual_args):
    #     names.append(val)

    # except:
    #   logging.error(obj + " can't have name")

    return toml.dumps(self._prepare(obj, True))

  def load(self, file_stream):
    return toml.load(file_stream)

  def loads(self, string):
    return toml.loads(string)

  def _prepare(self, obj, mode=False):
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

      if mode:
        return { 
          "name" : obj
        }
      else :
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
      try:
        s_obj = str(base64.b64encode(pickle.dumps(obj)))

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