from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def hello_world(request):
    return Response("Hello, World!")


@api_view(['GET'])
def hello_world_json(request):
    data = {
        "message": "Hello, World!",
        "status": "success",
    }

    return Response(data)

@api_view(['GET'])
def list_json_view(request):
    data = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
        {"id": 3, "name": "Jim"},
    ]

    return Response(data)

@api_view(['GET'])
def ping(request):
    message = request.GET.get('message', 'Hello, World!')

    return Response({
        "message": message,
        "status": "success",
    })

@api_view(['POST'])
@parser_classes([JSONParser])
def ping_post(request):
    message = request.data.get('message', 'Hello, World!')

    return Response({
        "message": message,
        "status": "success",
    })
