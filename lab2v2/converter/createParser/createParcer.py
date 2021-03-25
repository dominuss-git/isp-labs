# import sys

# sys.path.append('../converter')

from services.Yaml import Yaml
from services.Json import Json
from services.Toml import Toml
from services.Pickle import Pickle
import base64
import pickle
import logging

class CreateSerializator:
  def serialize(self, obj, /, format='JSON',  * , file_path=None):
    self.serializer = None
    # print(format, obj, end=" ")

    if format == 'JSON':
      self.serializer = Json()
    elif format == 'YAML':
      self.serializer = Yaml()
    elif format == 'TOML':
      self.serializer = Toml()
    elif format == 'PICKLE':
      self.serializer = Pickle()
    else:
      logging.error(f"Unsuported type {format}")
      exit()

    if file_path is None:
      return self.serializer.dumps(obj)
    else:
      with open(file_path, 'w', encoding='UTF-8') as f:
        return self.serializer.dump(obj, f)
    


class CreateDeserializator:
  def deserialize(self, string, /, format='JSON',  * , file_mode=False, normalize=False):
    self.deserializer = None
    
    if format == 'JSON':
      self.deserializer = Json()
    elif format == 'YAML':
      self.deserializer = Yaml()
    elif format == 'TOML':
      self.deserializer = Toml()
    elif format == 'PICKLE':
      self.deserializer = Pickle()
    else:
      logging.error(f"Unsupported type {format}")
      exit()

    if file_mode is False:
      out = self.deserializer.loads(string)
    else:
      with open(string, 'r', encoding='UTF-8') as f:
        out = self.deserializer.load(f)

    if normalize and format != 'PICKLE':
      return self.normalizer(out)
    else:
      return out

  def normalizer(self, obj):
    if isinstance(obj, (bool, str, int, float, complex)):
      return obj
    
    elif isinstance(obj, list):
      for index in range(len(obj)):
        obj[index] = self.normalizer(obj[index])

      return obj

    elif isinstance(obj, dict):
      if '__base64__' in obj.keys():
        return pickle.loads(base64.b64decode(obj['__base64__']))

      else:
        for key, value in obj.items():
          obj[key] = self.normalizer(value)

        return obj

