from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def hello_world(request):
    """
    단순히 Text를 반환하는 뷰
    """
  
    return HttpResponse("Hello, World!")


def hello_world_json(request):
    """
    JSON 형식으로 응답하는 뷰
    """
    data = {
        "message": "Hello, World!",
        "status": "success",
    }
    return JsonResponse(data)


def list_json_view(request):
    """
    JSON 형식으로 리스트 데이터 응답
    """
    data = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
        {"id": 3, "name": "Jim"},
    ]
    # dirtionary 형태가 아니라면 safe=False를 설정해야 함
    return JsonResponse(data, safe=False) 


def ping(request):
    """
    핑 요청에 대한 응답
    """
    request_data = request.GET.get('message', 'Hello, World!')

    return JsonResponse({
        "message": request_data,
        "status": "success",
    })


@csrf_exempt
def ping_post(request):
    """
    POST 요청에 대한 응답
    """
    request_data = request.body.decode('utf-8')
    json_data = json.loads(request_data)

    return JsonResponse({
        "message": json_data.get('message', 'Hello, World!'),
        "status": "success",
    })

