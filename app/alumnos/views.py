from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from alumnos.models import Alumno
from djongo import models
from rest_framework.fields import Field, SerializerMethodField
from rest_meets_djongo.serializers import DjongoModelSerializer



class AlumnoSerializer(DjongoModelSerializer):

    class Meta:
        model = Alumno
        fields = '__all__'

class AlumnosSearchListView(ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    http_method_names = ['get']
    search_fields = ('nombre', 'primer_apellido')

class AlumnosDetailView(ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def get_object(self, pk):
        try:
            return Alumno.objects.filter({'_id': models.ObjectIdField(pk)})
        except:
            raise Http404

    def get(self, request, pk, format=None):
        alumno = Alumno.objects.get(pk=pk)
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        alumno = Alumno.objects.get(pk=pk)
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        alumno = Alumno.objects.get(pk=pk)
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, pk, format=None):
        alumno = Alumno.objects.get(pk=pk)
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)