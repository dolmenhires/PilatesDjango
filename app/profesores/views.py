from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from djongo import models
from profesores.models import Profesor
from rest_framework.fields import Field, SerializerMethodField
from rest_meets_djongo.serializers import DjongoModelSerializer

# Create your views here.
class ProfesorSerializer(DjongoModelSerializer):

    class Meta:
        model = Profesor
        fields = '__all__'

class ProfesoresSearchListView(ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    http_method_names = ['get']

class ProfesoresDetailView(ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    def get_object(self, pk):
        try:
            return Profesor.objects.filter({'_id': models.ObjectIdField(pk)})
        except:
            raise Http404

    def get(self, request, pk, format=None):
        profesor = Profesor.objects.get(pk=pk)
        serializer = ProfesorSerializer(profesor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profesor = Profesor.objects.get(pk=pk)
        serializer = ProfesorSerializer(profesor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, pk, format=None):
        profesor = Profesor.objects.get(pk=pk)
        serializer = ProfesorSerializer(profesor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profesor = Profesor.objects.get(pk=pk)
        profesor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)