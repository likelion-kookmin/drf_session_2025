from django.shortcuts import render
from .models import Article
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    articles = Article.objects.all()

    response_data = {
        "result": [
            {
                "id": article.id,
                "title": article.title,
            } 
            for article in articles
        ]
    }

    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})

def show(request, id):
    article = Article.objects.get(id=id)

    response_data = {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "created_at": article.created_at,
        "updated_at": article.updated_at,
    }

    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def create(request):
    if request.method != 'POST':
        return HttpResponseNotFound()

    try:
        data = json.loads(request.body.decode('utf-8'))
        title = data.get('title', '')
        content = data.get('content', '')
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')
    except Exception as e:
        return HttpResponseBadRequest(f'Error: {e}')

    article = Article.objects.create(title=title, content=content)

    response_data = {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "created_at": article.created_at,
        "updated_at": article.updated_at,
    }

    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def update(request, id):
    if request.method != 'PUT':
        return HttpResponseNotFound()
    
    try:
        article = Article.objects.get(id=id)
        request_data = request.body.decode('utf-8')
        json_data = json.loads(request_data)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')
    except Article.DoesNotExist:
        return HttpResponseNotFound()
    except Exception as e:
        return HttpResponseBadRequest(f'Error: {e}')

    title = json_data.get('title', '')
    content = json_data.get('content', '')

    article.title = title
    article.content = content
    article.save()

    response_data = {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "created_at": article.created_at,
            "updated_at": article.updated_at,
    }

    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})
    


@csrf_exempt
def destroy(request, id):
    if request.method != 'DELETE':
        return HttpResponseNotFound()
    
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return HttpResponseNotFound()
    except Exception as e:
        return HttpResponseBadRequest(f'Error: {e}')

    article.delete()
    return JsonResponse({
        "message": "Article deleted successfully"
    }, json_dumps_params={'ensure_ascii': False})
