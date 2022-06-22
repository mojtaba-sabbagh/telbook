from django.urls import path
from .views import name_search

urlpatterns = [
    path('byname/', name_search, name='namesearch'),
]