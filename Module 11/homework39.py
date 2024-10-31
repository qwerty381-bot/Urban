def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    attributes = [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
    info['attributes'] = attributes
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['methods'] = methods
    info['module'] = obj.__class__.__module__
    return info

number_info = introspection_info(42)
print(number_info)
