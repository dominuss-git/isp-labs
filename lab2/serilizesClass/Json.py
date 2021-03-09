class Json:

  def dump(self, obj_f, fl):
    print(obj_f)
    class_name = [obj for obj in dir(obj_f) if not obj.startswith("__")]
    print(class_name)
    # obj = obj.__getattribute__(class_name[0])

    # print(fields)
    with open(fl, 'w') as writer:
      writer.write("{\n")
      for name in class_name:
        obj = obj_f.__getattribute__(name)
        fields = [field for field in dir(obj) if not field.startswith("__") if not callable(getattr(obj, field))]
        if not isinstance(obj, (str, dict, set, tuple, bool, list)):
          writer.write('"' + obj.__name__ + '" : {\n  "type" : "class",\n  "val" : {\n')
          for field in fields:
            value = obj.__getattribute__(obj, field)
            writer.write(f"  \"{field}\" : {self._PrettyPrint(value, count = 6)},\n")
          writer.write('  }\n},\n')
        else:
          # name = lambda x:[n for n in globals() if id(globals()[n]) == id(x)]
          # print(name(obj))
          writer.write(f"  \"{name}\" : {self._PrettyPrint(obj, count = 4)},\n")
      writer.write("}")

    # print(obj, fields, fl, sep="\n")

# --------------------------------------------------------------------------------------------------------------

  def dumps(self, obj_f):
    class_name = [obj for obj in dir(obj_f) if not obj.startswith("__")]
    # obj = obj.__getattribute__(class_name[0])

    # fields = [field for field in dir(obj) if not field.startswith("__") if not callable(getattr(obj, field))]
    output = "{"
    for name in class_name:
      obj = obj_f.__getattribute__(name)
      fields = [field for field in dir(obj) if not field.startswith("__") if not callable(getattr(obj, field))]

      if not isinstance(obj, (str, dict, set, tuple, bool, list)):
        output += '"name":"' + obj.__name__ + '"{"type":"class","val":{'
        for field in fields:
          value = obj.__getattribute__(obj, field)
          output += f"\"{field}\":{self._ObjToJsonString(value)},"
        output += '}},'
      else:
        # name = lambda x:[n for n in globals() if id(globals()[n]) == id(x)][0]
        output += f"\"{name}\":{self._ObjToJsonString(obj)},"
    output += "}"
    return output

# --------------------------------------------------------------------------------------------------------------

  def load(self, fl):
    pass

# --------------------------------------------------------------------------------------------------------------

  def loads(self, string):
    # a = type("my", (), {})
    for index in range(len(string)):
      if not string[index] == " " or \
      string[index] == "\n":
        print(string[index])

    
# --------------------------------------------------------------------------------------------------------------
  
  # def _UnPack(self, string):
  #   null = None
  #   true = True
  #   false = False
  #   obj = eval(string)

  #   for key, val in obj.items():
  #     print(key, val, sep="   ---   ")

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

    elif type(value) is list:
      value2 = "["

      for val in value:
        if isinstance(val, (str, dict, set, tuple, bool, list)) or \
        val is None:
          val = self._PrettyPrint(val, count = count + 2)
        value2 += f"{val},"
      value = value2[:-1] + "]"
        
    elif type(value) is set:
      value2 = "{\n" + indent + "\"type\" : \"set\",\n" + indent + "\"val\" : ["

      for val in value:
        if isinstance(val, (str, bool)) or \
        val is None:
          val = self._PrettyPrint(val,count = count + 2)
        value2 += f"{val},"
      value = value2[:-1] + "]\n" + indent + "}"

    elif type(value) is tuple:
      value2 = "{\n" + indent + "\"type\": \"tuple\",\n" + indent + "\"val\" : ["

      for val in value:
        if isinstance(val, (str, dict, set, tuple, bool, list)) or \
        val is None:
          val = self._PrettyPrint(val, count = count + 2)

        value2 += f"{val},"
      value = value2[:-1] + "]\n" + indent + "}"
      
    elif type(value) is dict:   
      value2 = ""

      for key, val in value.items():
        if isinstance(val, (str, dict, set, tuple, bool, list)) or \
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

    elif type(value) is list:
      value2 = "["

      for val in value:
        if isinstance(val, (str, dict, set, tuple, bool, list)) or \
        val is None:
          val = self._ObjToJsonString(val)
        value2 += f"{val},"
      value = value2[:-1] + "]"

    elif type(value) is set:
      value2 = "{\"type\":\"set\",\"val\" : ["

      for val in value:
        if isinstance(val, (str, bool)) or \
        val is None:
          val = self._ObjToJsonString(val)
        value2 += f"{val},"
      value = value2[:-1] + "]}"

    elif type(value) is tuple:
      value2 = "{\"type\":\"tuple\",\"val\":["

      for val in value:
        if isinstance(val, (str, dict, set, tuple, bool, list)) or \
        val is None:
          val = self._ObjToJsonString(val)

        value2 += f"{val},"
      value = value2[:-1] + "]}"

    elif type(value) is dict:   
      value2 = ""

      for key, val in value.items():
        if isinstance(val, (str, dict, set, tuple, bool, list)) or \
        val is None:
          val = self._ObjToJsonString(val)

        value2 += f"\"{key}\" : {val},"

      value = "{" + value2[:]
      value += "}"
    return value
