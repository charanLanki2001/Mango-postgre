from django.urls import path
from . import views

urlpatterns = [
    path('your-view/', views.your_view, name='your_view'),
    path('admin_login/', views.admin_login, name='admin_login'),
]