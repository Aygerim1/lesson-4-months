from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create_view, name='post_create'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]
