# ./../labs/lab2/prog.py /home/dominuss/test/test.py "$(cat dfd.json)"
# ./../labs/lab2/prog.py /home/dominuss/test/test2.py dfd.json -s -f
import pickle
import inspect
import base64
import types
import importlib.machinery as imprt

class Json:

  def dump(self, obj_f, fl):
    print(obj_f)
    # class_name = [obj for obj in dir(obj_f) if not obj.startswith("__") \
    #   if not obj.startswith("Check") \
    #   if not obj.startswith("argparse") \
    #   if not obj.startswith("args") \
    #   if not obj.startswith("parser")]
    # print(class_name)
    # obj = obj.__getattribute__(class_name[0])

    # print(fields)
    with open(fl, 'w') as writer:
      writer.write("{\n")
      # for name in class_name:
      # obj = obj_f.__getattribute__(name)
      # print(obj)
      fields = [field for field in dir(obj_f) if not field.startswith("__")]
      if type(obj_f) == types.FunctionType:
        writer.write(f"  \"{func}\" : {self._PrettyPrint(obj_f, count = 4)},\n")

      elif not isinstance(obj_f, (str, dict, set, tuple, bool, list, int, float)) and \
        not obj_f is None:
        writer.write('"' + "name" + '" : {\n  "type" : "class",\n  "name" : "' + obj_f.__class__.__name__ + '",\n  "val" : {\n')

        for field in fields:
          value = obj_f.__getattribute__(field)
          writer.write(f"  \"{field}\" : {self._PrettyPrint(value, count = 6)},\n")
        writer.write('  }\n},\n')
      else:
        writer.write(f"  \"name\" : {self._PrettyPrint(obj, count = 4)},\n")
      writer.write("}")

    # print(obj, fields, fl, sep="\n")

# --------------------------------------------------------------------------------------------------------------

  def dumps(self, obj_f):
    # class_name = [obj for obj in dir(obj_f) if not obj.startswith("__") \
    #   if not obj.startswith("Check") \
    #   if not obj.startswith("argparse") \
    #   if not obj.startswith("args") \
    #   if not obj.startswith("parser")]

    # print("ok")
    # obj = obj.__getattribute__(class_name[0])

    # fields = [field for field in dir(obj) if not field.startswith("__") if not callable(getattr(obj, field))]
    output = "{"
    # for name in class_name:
      # obj = obj_f.__getattribute__(name)
    fields = [field for field in dir(obj_f) if not field.startswith("__")]
    if type(obj_f) == types.FunctionType:
        output += (f"  \"name\" : {self._ObjToJsonString(obj_f)},")

    elif not isinstance(obj_f, (str, dict, set, tuple, bool, list, int, float)) and \
      not obj_f is None:
      output += '"' + "name" + '":{"type":"class","name":"'+ obj_f.__class__.__name__ +'","val":{'
      for field in fields:
        value = obj_f.__getattribute__(field)
        # print(value, field, type(value), value.__class__)
        output += f"\"{field}\":{self._ObjToJsonString(value)},"
      output += '}},'
    else:
      # name = lambda x:[n for n in globals() if id(globals()[n]) == id(x)][0]
      output += f"\"name\":{self._ObjToJsonString(obj_f)},"
    output += "}"
    return output

# --------------------------------------------------------------------------------------------------------------

  def load(self, fl):
    string_for_deserializetion = ""
    real_count = 1
    name = ""
    obj = []
    print(fl)

    # normalize input string
    ok = False
    with open(fl, "r") as f:
      for val in f.read():
        if (val != " " and \
          val != "\n" and \
          val != "\t") or ok:
          if string[index] == '"':
            if ok:
              ok = False
            else:
              ok = True
          string_for_deserializetion += val

    # print(string_for_deserializetion)

    # normalize input string
    if string_for_deserializetion[0] != '{' or \
      string_for_deserializetion[len(string_for_deserializetion) - 1] != '}':
      print("76extept is not json type")
      exit()
    else:
      string_for_deserializetion = string_for_deserializetion[1:len(string_for_deserializetion) - 1]

    # print(string_for_deserializetion)

    for index in range(len(string_for_deserializetion)):
      if index != real_count - 1:
        continue
      
      elif string_for_deserializetion[index] == '"':
        name, ind = self._StrUnPack(string_for_deserializetion[index:])
        real_count += ind
        continue

      elif string_for_deserializetion[index] == ':':
        if string_for_deserializetion[index + 1] == '"': # string
          value, ind = self._StrUnPack(string_for_deserializetion[index + 1:])
          real_count += ind + 1
          obj.append([name, value])
          continue
          
        elif 48 <= ord(string_for_deserializetion[index + 1]) <= 57:
          value, ind = self._ValUnPack(string_for_deserializetion[index + 1:]) # val
          real_count += ind + 1
          obj.append([name, value])
          continue

        elif string_for_deserializetion[index + 1] == '[':
          value, ind = self._ListUnPack(string_for_deserializetion[index + 1:]) # list
          real_count += ind + 1
          obj.append([name, value])
          continue

        elif string_for_deserializetion[index + 1] == "f" or \
          string_for_deserializetion[index + 1] == "n" or \
          string_for_deserializetion[index + 1] == "t":

          value, ind = self._BoolUnPack(string_for_deserializetion[index + 1:]) # bool
          real_count += ind + 1
          obj.append([name, value])
          continue

        elif string_for_deserializetion[index + 1] == '{':
          value, ind = self._CheckDificultObject(string_for_deserializetion[index + 1:]) # type
          real_count += ind + 1
          obj.append([name, value])
          continue


      # print(string_for_deserializetion[index], sep="")
      real_count += 1
    
    # print()
    return(obj)

# --------------------------------------------------------------------------------------------------------------

  def loads(self, string):
    string_for_deserializetion = ""
    real_count = 1
    name = ""
    obj = []

    # normalize input string
    ok = False
    for index in range(len(string)):
      if (string[index] != " " and \
        string[index] != "\n" and \
        string[index] != "\t") or ok:
        if string[index] == '"':
          if ok:
            ok = False
          else:
            ok = True
        string_for_deserializetion += string[index]

    # print(string_for_deserializetion)

    # normalize input string
    if string_for_deserializetion[0] != '{' or \
      string_for_deserializetion[len(string_for_deserializetion) - 1] != '}':
      print("76extept is not json type")
      exit()
    else:
      string_for_deserializetion = string_for_deserializetion[1:len(string_for_deserializetion) - 1]

    # print(string_for_deserializetion)

    for index in range(len(string_for_deserializetion)):
      if index != real_count - 1:
        continue
      
      elif string_for_deserializetion[index] == '"':
        name, ind = self._StrUnPack(string_for_deserializetion[index:])
        real_count += ind
        continue

      elif string_for_deserializetion[index] == ':':
        if string_for_deserializetion[index + 1] == '"': # string
          value, ind = self._StrUnPack(string_for_deserializetion[index + 1:])
          real_count += ind + 1
          obj.append([name, value])
          continue
          
        elif 48 <= ord(string_for_deserializetion[index + 1]) <= 57:
          value, ind = self._ValUnPack(string_for_deserializetion[index + 1:]) # val
          real_count += ind + 1
          obj.append([name, value])
          continue

        elif string_for_deserializetion[index + 1] == '[':
          value, ind = self._ListUnPack(string_for_deserializetion[index + 1:]) # list
          real_count += ind + 1
          obj.append([name, value])
          continue

        elif string_for_deserializetion[index + 1] == "f" or \
          string_for_deserializetion[index + 1] == "n" or \
          string_for_deserializetion[index + 1] == "t":

          value, ind = self._BoolUnPack(string_for_deserializetion[index + 1:]) # bool
          real_count += ind + 1
          obj.append([name, value])
          continue

        elif string_for_deserializetion[index + 1] == '{':
          value, ind = self._CheckDificultObject(string_for_deserializetion[index + 1:]) # type
          real_count += ind + 1
          obj.append([name, value])
          continue


      # print(string_for_deserializetion[index], sep="")
      real_count += 1
    
    # print()
    return (obj)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

  def _StrUnPack(self, string):
    output = ""
    # print(string)
    if string[0] == '"':
      for index in range(1, len(string)):
        if string[index] == '"':
          return output, index + 1
        output += string[index]
      else:
        print("107extept in _StrUnPack input error")
        exit()
    else:
      print("100extept in _StrUnPack is not string")
      exit()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

  def _ListUnPack(self, string):
    x = []
    real_count = 2

    if (string[0] == '['):
      for index in range(1, len(string)):
        if index != real_count - 1:
          continue

        elif string[index] == ']':
          return x, index + 1
  
        elif string[index] != ',':
          if string[index] == '"':
            value, ind = self._StrUnPack(string[index:])
            x.append(value)
            real_count += ind
            continue

          elif 48 <= ord(string[index]) <= 57:
            value, ind = self._ValUnPack(string[index:])
            x.append(value)
            real_count += ind
            continue

          elif string[index] == 'n' or \
            string[index] == 't' or \
            string[index] == 'f':

            value, ind = self._BoolUnPack(string[index:])
            x.append(value)
            real_count += ind
            continue

          elif string[index] == '[':
            value, ind = self._ListUnPack(string[index:])
            x.append(value)
            real_count += ind
            continue

          elif string[index] == '{':
            value, ind = self._CheckDificultObject(string[index:])
            x.append(value)
            real_count += ind
            continue

        real_count += 1
        # print(string[index], end="", sep="")
      else:
        print("159extept in ListUnPack error input")
        exit()
    else:
      print("135extept in ListInPack is not list")
      exit()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

  def _ValUnPack(self, string):
    dat = False
    out = ""

    # print(string)
    for index in range(len(string)):
      if string[index] == '.':
        if dat:
          print("188extept in _ValUnPack error input")
          exit()
        
        else:
          out += string[index]
          dat = True
        
      elif string[index] == ',' or string[index] == ']' or string[index] == '}':
        if dat:
          return float(out), index
        
        else:
          return int(out), index

      elif 48 <= ord(string[index]) <= 57: 
        out += string[index]

      else:
        print("204 extept in ValUnPack input error")
        exit()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

  def _BoolUnPack(self, string):
    val = string[0 : 4]
    
    if val == 'null':
      return None, 4
    
    elif val == 'true':
      return True, 4

    elif string[0 : 5] == 'false':
      return False, 5

    else:
      print("243 extept in BoolUnPack is not bool")
      exit()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

  def _CheckDificultObject(self, string):
    if string[1] == '"':
      value, ind = self._StrUnPack(string[1:])
      if value == 'type':
        if string[ind + 2] == '"':
          value, ind2 = self._StrUnPack(string[ind + 2:])
          ind += ind2 + 2
          if value == 'tuple':            
            if string[ind + 1] == '"':
              value, ind2 = self._StrUnPack(string[ind + 1:])

              ind += ind2 + 1

              if value == 'val':
                if string[ind + 1] == '[':
                  value, ind2 = self._ListUnPack(string[ind + 1:])
                  ind += ind2 + 1
                  if string[ind] == '}':
                    return tuple(value), ind + 1
                  else:
                    print("280extept in CheckDificultObject error input")
                    exit()
                else:
                  print("281extept in CheckDificultObject error input")
                  exit()
              else:
                value, ind2 = self._DictUnPack(string)
                return value, ind2
            else:
              value, ind2 = self._DictUnPack(string)
          elif value == 'set':
            if string[ind + 1] == '"':
              value, ind2 = self._StrUnPack(string[ind + 1:])
              ind += ind2 + 1

              if value == 'val':
                if string[ind + 1] == '[':
                  value, ind2 = self._ListUnPack(string[ind + 1:])
                  ind += ind2 + 1

                  if string[ind] == '}':
                    try:
                      x = set(value)
                      return x, ind + 1
                    except TypeError:
                      print(f"302extept Syntax error: unpack unhasheble type to set")
                      exit()
                  else:
                    print("381extept in CheckDificultObject error input")
                    exit()
                else:
                  print("303extept in CheckDificultObject error input")
                  exit()
              else:
                value, ind2 = self._DictUnPack(string)
                return value, ind2
            else:
              value, ind2 = self._DictUnPack(string)
              return value, ind2

          elif value == 'class':
            if string[ind + 1] == '"':
              name, ind2 = self._StrUnPack(string[ind + 1:])
              ind += ind2 + 1

              if name == "name":
                if string[ind + 1] == '"':
                  classname, ind2 = self._StrUnPack(string[ind + 1:])
                  ind += ind2 + 1

                  if string[ind + 1] == '"':
                    name, ind2 = self._StrUnPack(string[ind + 1:])
                    ind += ind2 + 1
                    if name == 'val':
                      value, ind2 = self._DictUnPack(string[ind + 1:])
                      ind += ind2
                      # print(string[ind: ind + 5])
                      if string[ind] == '}' and string[ind + 1] == '}':
                        return type(classname, (), value), ind + 2
                      else:
                        print(f"344extept in CheckDificultValue syntax error {string[ind - 4:ind + 5]}")
                        exit()
                    else:
                      value, ind2 = self._DictUnPack(string)
                      return value, ind2 
                  else:
                    value, ind2 = self._DictUnPack(string)
                    return value, ind2 
                else:
                  value, ind2 = self._DictUnPack(string)
                  return value, ind2 
              else:
                value, ind2 = self._DictUnPack(string)
                return value, ind2       
            else:
              value, ind2 = self._DictUnPack(string)
              return value, ind2
          elif value == 'function':
            if string[ind + 1] == '"':
              name, ind2 = self._StrUnPack(string[ind + 1:])
              ind += ind2 + 1

              if name == "name":
                if string[ind + 1] == '"':
                  funcname, ind2 = self._StrUnPack(string[ind + 1:])
                  ind += ind2 + 1

                  if string[ind + 1] == '"':
                    name, ind2 = self._StrUnPack(string[ind + 1:])
                    ind += ind2 + 1
                    if string[ind + 1] == '[':
                      code, ind2 = self._ListUnPack(string[ind +1:])
                      ind += ind2 + 1
                      if string[ind + 1] == '"':
                        name, ind2 = self._StrUnPack(string[ind +1:])
                        ind += ind2 + 1
                        if name == "base64":
                          if string[ind + 1] == '"':
                            base, ind2 = self._StrUnPack(string[ind +1:])
                            ind += ind2 + 1
                            print(base)
                            func_code = ""

                            for val in code:
                              func_code += val + "\n"

                            base = base64.b64decode(base)

                            return pickle.loads(base), ind + 1

                            # return [types.FunctionType, funcname, base, func_code], ind + 1
                            print(base)

                            # obj = pickle.loads(base)
                          else:
                            value, ind2 = self._DictUnPack(string)
                            return value, ind2
                        else:
                          value, ind2 = self._DictUnPack(string)
                          return value, ind2
                      else:
                        value, ind2 = self._DictUnPack(string)
                        return value, ind2
                    else:
                      value, ind2 = self._DictUnPack(string)
                      return value, ind2
                  else:
                    value, ind2 = self._DictUnPack(string)
                    return value, ind2 
                else:
                  value, ind2 = self._DictUnPack(string)
                  return value, ind2
              else:
                value, ind2 = self._DictUnPack(string)
                return value, ind2
            else:
              value, ind2 = self._DictUnPack(string)
              return value, ind2
          else:
            value, ind2 = self._DictUnPack(string)
            return value, ind2
        else:
          value, ind2 = self._DictUnPack(string)
          return value, ind2
      else:
        value, ind2 = self._DictUnPack(string)
        return value, ind2
    else:
      print("284extept in CheckDificultObject error input")
      exit()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

  def _DictUnPack(self, string):
    if string[0] == '{':
      real_count = 2
      x = dict()

      for index in range(1, len(string)):
        if index != real_count - 1:
          continue

        elif string[index] == '}':
          return x, index + 1

        elif string[index] == '"':
          name, ind = self._StrUnPack(string[index:])
          real_count += ind
          continue

        elif string[index] == ':':
          if string[index + 1] == '[':
            value, ind = self._ListUnPack(string[index + 1:])
            x[name] = value
            real_count += ind + 1
            continue

          elif string[index + 1] == '"':
            value, ind = self._StrUnPack(string[index + 1:])
            x[name] = value
            real_count += ind + 1
            continue

          elif 48 <= ord(string[index + 1]) <= 57:
            value, ind = self._ValUnPack(string[index + 1:])
            x[name] = value
            real_count += ind + 1
            continue

          elif string[index + 1] == "f" or \
            string[index + 1] == "n" or \
            string[index + 1] == "t":

            value, ind = self._BoolUnPack(string[index + 1:]) # bool
            real_count += ind + 1
            x[name] = value
            continue
          
          elif string[index + 1] == '{':
            value, ind = self._CheckDificultObject(string[index + 1:]) # type
            real_count += ind + 1
            x[name] = value
            continue

        real_count += 1
        # print(string[index], sep="", end="")
    else:
      print("312extept in DictUnPack is not dictionary")
      exit()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------

  def _PrettyPrint(self, value, *, count=2):
    indent = ""   
    for i in range(count - 2):
      indent += " "

    if type(value) is str:
      value = f'"{value[:]}"'

    elif value is None:
      value = "null"

    elif value is False:
      value = "false"

    elif value is True:
      value = "true"

    elif type(value) == types.FunctionType or \
      type(value) == types.MethodDescriptorType :
      # print(str(base64.b64encode(pickle.dumps(value))))

      value2 = inspect.getsource(value)
      value3 = indent + '"'
      count = 0
      for char in value2:
        count += 1
        if char == '\n':
          if count != len(value2):
            value3 += '",' + char + indent + '"'
          else:
            value3 += '"'
            break
        else:
          value3 += char 
      # print(pickle.dumps(value))
      base = str(base64.b64encode(pickle.dumps(value, fix_imports=True)))
      # print(base)
      base = base[2: len(base) - 1]
      # print(base)
      value = '{\n' + indent +'"type": "function",\n' + indent + '"name": "' + value.__name__ + '",\n' + indent + '"code": [\n'\
        + value3 + '],\n' + indent + f'"base64": "{base}"' + '\n}'

    elif type(value) is list:
      value2 = "["

      for val in value:
        if isinstance(val, (str, dict, set, tuple, bool, list, types.FunctionType)) or \
        val is None:
          val = self._PrettyPrint(val, count = count + 2)
        value2 += f"{val},"
      value = value2[:-1] + "]"
        
    elif type(value) is set:
      value2 = "{\n" + indent + "\"type\" : \"set\",\n" + indent + "\"val\" : ["

      for val in value:
        if isinstance(val, (str, bool, tuple)) or \
        val is None:
          val = self._PrettyPrint(val,count = count + 2)
        value2 += f"{val},"
      value = value2[:-1] + "]\n" + indent + "}"

    elif type(value) is tuple:
      value2 = "{\n" + indent + "\"type\": \"tuple\",\n" + indent + "\"val\" : ["

      for val in value:
        if isinstance(val, (str, dict, set, tuple, bool, list, types.FunctionType)) or \
        val is None:
          val = self._PrettyPrint(val, count = count + 2)

        value2 += f"{val},"
      value = value2[:-1] + "]\n" + indent + "}"
      
    elif type(value) is dict:   
      value2 = ""

      for key, val in value.items():
        if isinstance(val, (str, dict, set, tuple, bool, list, types.FunctionType)) or \
        val is None:
          val = self._PrettyPrint(val, count = count + 2)

        value2 += indent + f"\"{key}\" : {val},\n"
      value = "{\n" + value2[:] + indent + "}"

    return value

# --------------------------------------------------------------------------------------------------------------

  def _ObjToJsonString(self, value):
    if type(value) is str:
      value = f'"{value[:]}"'

    elif value is None:
      value = "null"

    elif value is False:
      value = "false"

    elif value is True:
      value = "true"

    elif type(value) == types.FunctionType:
      value2 = inspect.getsource(value)
      value3 = '"'
      count = 0

      print("hi")

      for char in value2:
        count += 1
        if char == '\n':
          if count != len(value2):
            value3 += '",' + '"'
          else:
            value3 += '"'
            break
        else:
          value3 += char 

      base = str(base64.b64encode(pickle.dumps(value)))
      # print(base)
      base = base[2: len(base) - 1]

      value = '{"type":"function","name":"' + value.__name__  + '","code":['\
        + value3 + '],' + f'"base64":"{base}"' + '}'

    elif type(value) is list:
      value2 = "["

      for val in value:
        if isinstance(val, (str, dict, set, tuple, bool, list, types.FunctionType)) or \
        val is None:
          val = self._ObjToJsonString(val)
        value2 += f"{val},"
      value = value2[:-1] + "]"

    elif type(value) is set:
      value2 = "{\"type\":\"set\",\"val\" : ["

      for val in value:
        if isinstance(val, (str, bool, tuple)) or \
        val is None:
          val = self._ObjToJsonString(val)
        value2 += f"{val},"
      value = value2[:-1] + "]}"

    elif type(value) is tuple:
      value2 = "{\"type\":\"tuple\",\"val\":["

      for val in value:
        if isinstance(val, (str, dict, set, tuple, bool, list, float, int, types.FunctionType)) or \
        val is None:
          val = self._ObjToJsonString(val)

        value2 += f"{val},"
      value = value2[:-1] + "]}"

    elif type(value) is dict:   
      value2 = ""

      for key, val in value.items():
        if isinstance(val, (str, dict, set, tuple, bool, list, float, int, types.FunctionType)) or \
        val is None:
          val = self._ObjToJsonString(val)

        value2 += f"\"{key}\" : {val},"

      value = "{" + value2[:]
      value += "}"
    
    return value

# --------------------------------------------------------------------------------------------------------------
