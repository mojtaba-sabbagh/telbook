from django.urls import path
from .views import name_search, dep_names

urlpatterns = [
    path('byname/', name_search, name='namesearch'),
    path('deps/', dep_names, name='depnames'),
]