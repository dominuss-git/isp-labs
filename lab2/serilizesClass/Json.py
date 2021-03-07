class Json:
  def dump(self, obj, fl):
    fields = [field for field in dir(obj) if not field.startswith("__") if not callable(getattr(obj, field))]

    with open(fl, 'w') as writer:
      writer.write("{\n")
      for field in fields:
        value = obj.__getattribute__(obj, field)
        writer.write(f"\"{field}\" : {self._PrettyPrint(value)},\n")
      writer.write("}")

    # print(obj, fields, fl, sep="\n")

# --------------------------------------------------------------------------------------------------------------

  def dumps(self, obj):
    fields = [field for field in dir(obj) if not field.startswith("__") if not callable(getattr(obj, field))]
    output = ""

    for field in fields:
      value = obj.__getattribute__(obj, field)
      # print(value)
      output += f"\"{field}\" : {self._ObjToJsonString(value)},"
    print(output)

# --------------------------------------------------------------------------------------------------------------

  def load(self, fl):
    pass

# --------------------------------------------------------------------------------------------------------------

  def loads(self, string):
    pass

# --------------------------------------------------------------------------------------------------------------

  def _PrettyPrint(self, value, count=2):
    indent = ""   
    for i in range(count - 2):
      indent += " "

    if type(value) is str:
      value = f'"{value[:]}"'

    elif type(value) is list:
      value2 = "["

      for val in value:
        if type(val) is str or \
        type(val) is dict or \
        type(val) is set or \
        type(val) is tuple or \
        type(val) is list:
          val = self._PrettyPrint(val, count = count + 2)
        value2 += f"{val},"
      value = value2[:-1] + "]"
        
    elif type(value) is set:
      value2 = "{\n" + indent + "\"type\" : \"set\",\n" + indent + "\"val\" : ["

      for val in value:
        if type(val) is str:
          val = self._PrettyPrint(val,count = count + 2)
        value2 += f"{val},"
      value = value2[:-1] + "]\n}"

    elif type(value) is tuple:
      value2 = "{\n" + indent + "\"type\": \"tuple\",\n" + indent + "\"val\" : ["

      for val in value:
        if type(val) is str or \
        type(val) is dict or \
        type(val) is set or \
        type(val) is tuple or \
        type(val) is list:
          val = self._PrettyPrint(val, count = count + 2)

        value2 += f"{val},"
      value = value2[:-1] + "]\n" + indent + "}"
      
    elif type(value) is dict:   
      value2 = ""

      for key, val in value.items():
        if type(val) is str or \
        type(val) is dict or \
        type(val) is set or \
        type(val) is tuple or \
        type(val) is list:
          val = self._PrettyPrint(val, count = count + 2)

        value2 += indent + f"\"{key}\" : {val},\n"
      value = "{\n" + value2[:] + indent + "}"

    return value

  def _ObjToJsonString(self, value):
    if type(value) is str:
      value = f'"{value[:]}"'

    elif type(value) is list:
      value2 = "["

      for val in value:
        if type(val) is str or \
        type(val) is dict or \
        type(val) is set or \
        type(val) is tuple or \
        type(val) is list:
          val = self._ObjToJsonString(val)
        value2 += f"{val},"
      value = value2[:-1] + "]"

    elif type(value) is set:
      value2 = "{\"type\" : \"set\",\"val\" : ["

      for val in value:
        if type(val) is str:
          val = self._ObjToJsonString(val)
        value2 += f"{val},"
      value = value2[:-1] + "]}"

    elif type(value) is tuple:
      value2 = "{\"type\": \"tuple\",\"val\" : ["

      for val in value:
        if type(val) is str or \
        type(val) is dict or \
        type(val) is set or \
        type(val) is tuple or \
        type(val) is list:
          val = self._ObjToJsonString(val)

        value2 += f"{val},"
      value = value2[:-1] + "]}"

    elif type(value) is dict:   
      value2 = ""

      for key, val in value.items():
        if type(val) is str or \
        type(val) is dict or \
        type(val) is set or \
        type(val) is tuple or \
        type(val) is list:
          val = self._ObjToJsonString(val)

        value2 += f"\"{key}\" : {val},"

      value = "{" + value2[:]
      value += "}"
    return value