import inspect
# from pprint import pprint

class MyClass:
    def __init__(self, name):
        self.name = name

object = MyClass('Robot')

def introspection_info(obj):
    result = {}
    result['type'] = type(obj)
    result['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__') and not callable(getattr(obj, attr))]
    result['methods'] = dir(obj)
    result['module'] = inspect.getmodule(obj)
    return result

object_info = introspection_info(object)
print(object_info)
# pprint(object_info)

number_info = introspection_info(42)
print(number_info)