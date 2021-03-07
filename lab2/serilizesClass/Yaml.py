class Yaml:
  def dump(self, obj, fl):
    fields = [field for field in dir(obj) if not field.startswith("__") if not callable(getattr(obj, field))]
    print(obj, fields, fl, sep="\n")
  def dumps(self, obj):
    fields = [field for field in dir(obj) if not field.startswith("__") if not callable(getattr(obj, field))]
    print(obj, fields, sep="\n")
  def load(self, fl):
    pass
  def loads(self, string):
    pass