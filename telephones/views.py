from django.shortcuts import render
from pyparsing import And
from sympy import re
from .models import Department, Profile, Position, Assign
from django.db.models import Q
from .serializers import AssignNameSerializer, DepNameSerializer
from django.http import JsonResponse
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
def name_search(request):
    """ search for name in specified area """

    qname = request.GET.get('q', '')
    dep = request.GET.get('dep', '')
    deps = []
    if dep != '':
        main_deps = Department.objects.select_related('super_dep').filter(super_dep=dep)
        sub_deps = [ Department.objects.select_related('super_dep').filter(super_dep=sub_dep) 
                     for sub_dep in main_deps]
        if sub_deps:
            union_sub_deps = sub_deps[-1]
            for sub_dep in sub_deps[:-1]: union_sub_deps = union_sub_deps | sub_dep
            deps = main_deps | union_sub_deps | Department.objects.filter(id=dep)
        else:
            deps = main_deps | Department.objects.filter(id=dep)
        qset = Assign.objects.select_related('position').filter(position__dep__in=deps).\
            select_related('position__owner').\
            filter(Q(position__owner__first_name__contains=qname) | 
                Q(position__owner__last_name__contains=qname)).order_by('position__owner__last_name')
    else:
        qset = Assign.objects.select_related('position__owner').\
            filter(Q(position__owner__first_name__contains=qname) | 
                Q(position__owner__last_name__contains=qname)).order_by('position__owner__last_name')
    serial_qset = AssignNameSerializer(qset, many=True)
    # return a Json response
    return JsonResponse(serial_qset.data, safe=False)

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
def dep_names(request):
    """  """
    level = request.GET.get('level', '')
    sdep = request.GET.get('super-dep', '')
    if (sdep == ''):
        qset = Department.objects.filter(level=level)
    else:
        qset = Department.objects.filter(level=level, super_dep=sdep)
    
    serial_qset = DepNameSerializer(qset, many=True)
    # return a Json response
    return JsonResponse(serial_qset.data, safe=False)