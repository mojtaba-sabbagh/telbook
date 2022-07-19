from django.urls import path, re_path
from .views import name_search, dep_names, dep_positions, post_search

urlpatterns = [
    re_path('byname/(?P<dep>\d+)/(?P<qname>[آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی a-zA-Z0]+)/', name_search, name='namesearch'),
    re_path('bypost/(?P<dep>\d+)/(?P<qpost>\w+)/', post_search, name='postsearch'),
    path('deps/', dep_names, name='depnames'),
    path('posts/', dep_positions, name='deppositions'),
]