import os
import importlib.machinery as imprt
from serilizesClass.Json import Json
from serilizesClass.Yaml import Yaml
from serilizesClass.Pickle import Pickle
from serilizesClass.Toml import Toml

def Check(args):
  path_to_obj = ""
  path_to_file = ""

  if args.file:
    if args.path_to_file is not None:
      path_to_file = os.path.abspath(args.path_to_file)
    else:
      print("error: ./path_to_file is not defined")
      return
  else:
    path_to_file = args.path_to_file

  if args.path_to_obj is not None:
    path_to_obj = os.path.abspath(args.path_to_obj)
  else:
    parser.error()

  index = path_to_obj.find(".")
  if index == -1:
    print(f"Unknown extension: {path_to_obj}")
    return
  extension1 = path_to_obj[index:]
  extension2 = False

  if args.file:
    index = path_to_file.find(".")
    if index == -1:
      print(f"error: unknown extension: {path_to_file}")
      return
    extension2 = path_to_file[index:].lower()

    if extension2 != ".json" and \
    extension2 != ".yaml" and \
    extension2 != ".p" and \
    extension2 != ".toml":
      print(f"error: unknown extension {extension2}")
      return
  
  if extension1 != ".py":
    print(f"error: extension ./path_to_obj must be '.py' \n ")
    return

  
  extension = ""
  if args.path_to_file != None:
    index = path_to_file.find(".")
    if index != -1:
      extension = path_to_file[index:].lower() 

  args.serialize(path_to_obj, path_to_file, extension2, extension)

# --------------------------------------------------------------------

def CheckSerialize(path_to_obj, path_to_file, file_mode, extension):
  # print(path_to_obj, path_to_file, file_mode, "serialize", sep="\n")

  try:
    obj = imprt.SourceFileLoader("my", path_to_obj).load_module()
  except:
    print("error: object is not defined")
    return
  if file_mode == False:
    path_to_file = False
  # print(obj_for_serialize, path_to_file, file_mode, sep="\n")
  CreateSerializator(obj, path_to_file, extension)
  
# ----------------------------------------------------------------------

def CheckDeserialize(path_to_obj, path_to_file, file_mode, extension):
  if file_mode != False:
    try:  
      with open(path_to_file, 'r') as file:
        pass
    except:
      print("error: no such file for deserializition")
      return
  else:
    path_to_obj = None
  CreateDeserializator(path_to_file, path_to_obj, extension)
  # print(path_to_obj, path_to_file, file_mode, "deserialize", sep="\n")

# ---------------------------------------------------------------------

def CreateSerializator(obj, path, extension):
  # print(extension)
  serializator = None
  if extension == ".p":
    serializator = Pickle()
  elif extension == ".yaml":
    serializator = Yaml()
  elif extension == ".toml":
    serializator = Toml()
  else:
    serializator = Json()

  # print(serializator)
  if path == False:
    print (serializator.dumps(obj))
  else:
    serializator.dump(obj, path)

# ----------------------------------------------------------------------

def CreateDeserializator(fl, obj, extension):
  if extension == ".p":
    serializator = Pickle()
  elif extension == ".yaml":
    serializator = Yaml()
  elif extension == ".toml" or fl[0] == "[":
    serializator = Toml()
  else:
    serializator = Json()
  
  # print(extension == "")
  # print(serializator)

  if extension == "":
    serializator.loads(fl)
    # print(strs_s)
  else:
    serializator.load(fl)

  # print(fl, obj, extension, sep="\n")