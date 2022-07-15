from django.urls import path, re_path
from .views import name_search, dep_names

urlpatterns = [
    re_path('byname/(?P<dep>\d+)/(?P<qname>\w+)/', name_search, name='namesearch'),
    path('deps/', dep_names, name='depnames'),
]