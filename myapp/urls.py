from django.urls import path
from .views import queens_attack

urlpatterns = [
    path('problem-1/', queens_attack, name='queens_attack'),
]