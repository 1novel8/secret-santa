# from functools import wraps
#
#
# def attribute_required(attribute_name):
#     def decorator(cls):
#         @wraps(cls, updated=())
#         class DecoratedClass(cls):
#             def __init__(self, *args, **kwargs):
#                 if getattr(self, attribute_name) is None:
#                     raise AttributeError(f"attribute '{attribute_name}' should not be None.")
#
#                 super().__init__(*args, **kwargs)
#
#         return DecoratedClass
#     return decorator
