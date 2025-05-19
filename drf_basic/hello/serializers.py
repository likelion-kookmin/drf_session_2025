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

# serializer = HelloSerializer(hello_1)
# print(serializer.data)
# # {'message': 'Hello, This is Serializer Example!', 'is_happy': True, 'created_at': '2025-05-19T01:09:14.272935Z'}

# serializer = HelloSerializer(hello_2)
# print(serializer.data)
# # {'message': 'Hello, This is Serializer Example 2!', 'is_happy': False, 'created_at': '2025-05-19T01:09:14.273271Z'}


# from rest_framework.renderers import JSONRenderer

# json = JSONRenderer().render(serializer.data)
# print(json)
# # b'{"message":"Hello, This is Serializer Example 2!","is_happy":false,"created_at":"2025-05-19T01:10:04.708837Z"}'

