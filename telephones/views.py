from django.shortcuts import render
from models import Profile
# Create your views here.

def name_search(qname, level1='', level2='', level3=''):
    """ search for name in specified area """
    Profile.objects.filter(Q() | Q())
