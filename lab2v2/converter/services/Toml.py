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
    return self._out(toml.load(file_stream), mode=True)

  def loads(self, string):
    return self._out(toml.loads(string), mode=True)

  def _out(self, obj, *, mode=False):
    if isinstance(obj, dict):
      if '__list__' in obj.keys():
        # print(obj)
        obj = pickle.loads(base64.b64decode(obj['__list__']))
        obj = self._out(obj)
        return obj

      if isinstance(obj, dict):
        if '__val__' in obj.keys():
          return obj['__val__']

        if '__NoneVal__' in obj.keys():
          # print(obj)
          return None

        for key, value in obj.items():
          # print(key)
          if isinstance(value, dict):
            # print(value, key)
            obj[key] = self._out(value)
            # print(obj[key])
            # print(obj)

          elif key == '__list__':
            obj[key] = self._out(obj[key])

        return obj

    if isinstance(obj, list):
      # print(obj, "1")
      for index in range(len(obj)):
        # print(obj[index])
        obj[index] = self._out(obj[index])
        # print(obj[index])

      return obj
    # print(obj)
    return obj


  def _prepare(self, obj, mode=False):
    if isinstance(obj, (int, float, int, bool, str)):
      if mode:
        return {
          "__val__" : obj, 
        }

      else:
        return obj

    elif obj is None:
      return {
          "__NoneVal__" : "None", 
      }

    elif isinstance(obj, (set, tuple)):
      s_obj = str(base64.b64encode(pickle.dumps(obj)))

      return {
        "__type__" : str(type(obj)),
        "__base64__" : s_obj[2:len(s_obj) - 1],
      }

    elif isinstance(obj, list):
      for index in range(len(obj)):
        obj[index] = self._prepare(obj[index])

      s_obj = str(base64.b64encode(pickle.dumps(obj)))

      return { 
        "__list__" : s_obj[2:len(s_obj) - 1]
      }
    
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