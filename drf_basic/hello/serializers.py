from rest_framework import serializers
from datetime import datetime

class Hello:
    def __init__(self, message, is_happy, created_at=None):
        self.message = message
        self.is_happy = is_happy
        self.created_at = created_at or datetime.now()
        self.dummy = "this is dummy data"
    

class HelloSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=100)
    is_happy = serializers.BooleanField()
    created_at = serializers.DateTimeField()

# hello_1 = Hello("Hello, This is Serializer Example!", True)
# hello_2 = Hello("Hello, This is Serializer Example 2!", False, datetime.now())

# serializer1 = HelloSerializer(hello_1)
# print(serializer1.data)
# # {'message': 'Hello, This is Serializer Example!', 'is_happy': True, 'created_at': '2025-05-19T01:09:14.272935Z'}

# serializer2 = HelloSerializer(hello_2)
# print(serializer2.data)
# # {'message': 'Hello, This is Serializer Example 2!', 'is_happy': False, 'created_at': '2025-05-19T01:09:14.273271Z'}


# from rest_framework.renderers import JSONRenderer

# json = JSONRenderer().render(serializer2.data)
# print(json)
# # b'{"message":"Hello, This is Serializer Example 2!","is_happy":false,"created_at":"2025-05-19T01:10:04.708837Z"}'


# ### Validation 예제
# data = {
#     'message': 'Hello, This is Serializer Example 3!',
#     'is_happy': 'THIS IS WRONG DATA',  # Boolean이어야 하는데 문자열을 전달
#     'created_at': datetime.now()
# }
# serializer3 = HelloSerializer(data=data)
# print(serializer3.is_valid())  # False
# print(serializer3.errors) 
# # {'is_happy': [ErrorDetail(string='Must be a valid boolean.', code='invalid')]}

