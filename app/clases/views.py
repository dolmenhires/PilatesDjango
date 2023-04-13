from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from clases.models import Clase
from djongo import models
from rest_framework.fields import Field, SerializerMethodField
from rest_meets_djongo.serializers import DjongoModelSerializer


class ClaseSerializer(DjongoModelSerializer):

    class Meta:
        model = Clase
        fields = '__all__'

class ClasesSearchListView(ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    http_method_names = ['get']

class ClasesDetailView(ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

    def get_object(self, pk):
        try:
            return Clase.objects.filter({'_id': models.ObjectIdField(pk)})
        except:
            raise Http404

    def get(self, request, pk, format=None):
        clase = Clase.objects.get(pk=pk)
        serializer = ClaseSerializer(clase)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        clase = Clase.objects.get(pk=pk)
        serializer = ClaseSerializer(clase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, pk, format=None):
        clase = Clase.objects.get(pk=pk)
        serializer = ClaseSerializer(clase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        clase = Clase.objects.get(pk=pk)
        clase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)