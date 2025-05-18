from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
    path('json/', views.hello_world_json),
    path('list/', views.list_json_view),
    path('ping/', views.ping),
    path('ping_post/', views.ping_post),
]
