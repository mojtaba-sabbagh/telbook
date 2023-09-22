from django.shortcuts import render
from pyparsing import And
from sympy import re
from .models import Department, PositionType, Profile, Position, Assign
from django.db.models import Q
from .serializers import AssignNameSerializer, DepNameSerializer, PositionTypeSerializer
from django.http import JsonResponse
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination

# Create your views here.

def departments(dep):
    main_deps = Department.objects.select_related('super_dep').filter(super_dep=dep)
    sub_deps = [ Department.objects.select_related('super_dep').filter(super_dep=sub_dep) 
                     for sub_dep in main_deps]
    if sub_deps:
        union_sub_deps = sub_deps[-1]
        for sub_dep in sub_deps[:-1]: union_sub_deps = union_sub_deps | sub_dep
        deps = main_deps | union_sub_deps | Department.objects.filter(id=dep)
    else:
        deps = main_deps | Department.objects.filter(id=dep)
    return deps

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
def name_search(request, dep, qname):
    """ search for name in specified area """

    qname = '' if qname == '0' else qname.strip()
    deps = []
    if dep != '0':
        deps = departments(dep)
        qset = Assign.objects.select_related('position').filter(position__dep__in=deps).\
            select_related('position__owner').\
            filter(Q(position__owner__first_name__contains=qname) | 
                Q(position__owner__last_name__contains=qname)).order_by('position__dep__level', 'position__dep__dep_name', 'position__position_type__level', 'position__position_type', 'position__owner__last_name')
    else:
        qset = Assign.objects.select_related('position__owner').\
            filter(Q(position__owner__first_name__contains=qname) | 
                Q(position__owner__last_name__contains=qname)).order_by('position__dep__level', 'position__dep__dep_name', 'position__position_type__level', 'position__position_type', 'position__owner__last_name')
    paginator = PageNumberPagination()
    context = paginator.paginate_queryset(queryset=qset, request=request)
    serial_qset = AssignNameSerializer(context, many=True)
    return paginator.get_paginated_response(serial_qset.data)

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


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
def dep_positions(request):
    """  """
    ids = Position.objects.select_related('position_type').all().values('position_type__id')
    qset = PositionType.objects.filter(id__in=ids)
    
    serial_qset = PositionTypeSerializer(qset, many=True)
    # return a Json response
    return JsonResponse(serial_qset.data, safe=False)

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
def post_search(request, dep, qpost):
    """ search for post in specified area """
    deps = []
    if dep != '0':
        deps = departments(dep)
        if qpost != '0':
            qset = Assign.objects.select_related('position').filter(position__dep__in=deps).\
                select_related('position__position_type').\
                filter(position__position_type=qpost).order_by('position__dep__dep_name', 'position__position_type', 'position__owner__last_name')
        else:
            qset = Assign.objects.select_related('position').filter(position__dep__in=deps).\
                select_related('position__position_type').order_by('position__dep__dep_name', 'position__position_type', 'position__owner__last_name')
    else:
        if qpost != '0':
            qset = Assign.objects.select_related('position').\
                filter(position__position_type=qpost).order_by('position__dep__dep_name', 'position__position_type', 'position__owner__last_name')
        else:
            qset = Assign.objects.select_related('position').order_by('position__dep__dep_name', 'position__position_type', 'position__owner__last_name')

    paginator = PageNumberPagination()
    context = paginator.paginate_queryset(queryset=qset, request=request)
    serial_qset = AssignNameSerializer(context, many=True)
    # return a Json response
    return paginator.get_paginated_response(serial_qset.data)