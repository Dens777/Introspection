def introspection_info(obj):

    obj_type = type(obj).__name__

    attributes = dir(obj)

    methods = [method for method in attributes if callable(getattr(obj, method))]

    module = obj.__class__.__module__

    id_item = id(obj)


    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module, 'id': id_item}

    return info

# Интроспекция числа
number_info = introspection_info(11102024)
print (number_info)

# Интроспекция строки
string_info = introspection_info('UrbanUniversity')
print(string_info)

# Интроспекция списка
list_info = introspection_info([1, 20, 4.0, 'Home_work, module Introspections'])
print(list_info)

# Интроспекция словаря
dict_info = introspection_info({'volume':12,'treble':3,'bass':-4})
print(dict_info)

