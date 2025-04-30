from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create_view, name='post_create'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('test/', views.test_view, name='test_view'),
]

