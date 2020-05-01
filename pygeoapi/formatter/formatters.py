from importlib import import_module

formatters = {} # key value pair of format: formatter class

def register(format_, formatterClass):
    formatters[format_] = formatterClass


# def get_collection_items_formatters(func):
#     def function_wrapper(*args, **kwargs):
#         print("Before calling " + func.__name__)
#         # format_ = args[2]
#         # print(kwargs)
#         # print(format_)
#         # print(kwargs)
#         format_ = args[2].get('f')
#         if isinstance(format_, str) and len(format_):
#             try:
#                 print('before import')
#                 formatter_ = import_module('pygeoapi.formatter.' + format_)
#                 print('after import')
#                 ret = formatter_.get_collection_items(func, *args, **kwargs)
#                 print('after call')
#             except:
#                 ret = func(*args, **kwargs)
#         else:
#             ret = func(*args, **kwargs)
#         print("After calling " + func.__name__)
#         return ret
#     return function_wrapper