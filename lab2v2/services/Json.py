import json
import pickle
import inspect
import base64
import types
import logging

class Json:
  def dump(self, obj, file_stream):
    json.dump(obj, file_stream, default=self._dificult_objects, indent=2)

  def dumps(self, obj):
    json.dumps(obj, default=self._dificult_objects)

  def load(self, file_stream):
    return json.load(file_stream)

  def loads(self, string):
    return json.loads(string)

  def _dificult_objects(self, obj):
    if isinstance(obj, (set, tuple)):
      s_obj = str(base64.b64encode(pickle.dumps(obj)))

      return {
        "__type__" : str(type(obj)),
        "__base64__" : s_obj[2:len(s_obj) - 1],
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

    else:
      # value = dict()
      try:
        fields = [field for field in dir(obj) if not field.startswith("__")]
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
        logging.error(repr(obj) + ' is not json serializable')
        exit()