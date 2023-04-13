from django.shortcuts import render

from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from actividades.models import Actividad
from djongo import models
from rest_framework.fields import Field, SerializerMethodField
from rest_meets_djongo.serializers import DjongoModelSerializer



class ActividadSerializer(DjongoModelSerializer):

    class Meta:
        model = Actividad
        fields = '__all__'

class ActividadesSearchListView(ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
    http_method_names = ['get']
    search_fields = ('nombre', 'descripcion')

class ActividadesDetailView(ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

    def get_object(self, pk):
        try:
            return Actividad.objects.filter({'_id': models.ObjectIdField(pk)})
        except:
            raise Http404

    def get(self, request, pk, format=None):
        actividad = Actividad.objects.get(pk=pk)
        serializer = ActividadSerializer(actividad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        actividad = Actividad.objects.get(pk=pk)
        serializer = ActividadSerializer(actividad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        actividad = Actividad.objects.get(pk=pk)
        serializer = ActividadSerializer(actividad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        actividad = Actividad.objects.get(pk=pk)
        actividad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

