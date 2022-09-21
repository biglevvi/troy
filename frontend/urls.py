from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.frontend, name='homepage'),
    # path('<str:pk>/', views.frontend, name='homepage'),
]
