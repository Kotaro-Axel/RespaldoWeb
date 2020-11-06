from .models import Alumno
from .serializers import AlumnoSerializer

from rest_framework import viewsets, views, filters, generics
from django.shortcuts import render

# Create your views here.

class AlumnoViewSet(viewsets.ModelViewSet):
    
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['schol_controll']
    ordering_fields = ['id']

class AlumnoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    search_fields = ['schol_controll']
