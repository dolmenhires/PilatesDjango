from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from matriculas.models import Matricula
from djongo import models
from rest_framework.fields import Field, SerializerMethodField
from rest_meets_djongo.serializers import DjongoModelSerializer



class MatriculaSerializer(DjongoModelSerializer):

    class Meta:
        model = Matricula
        fields = '__all__'

class MatriculasSearchListView(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get']

class MatriculasDetailView(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    def destroy(self, request, pk):
        try:
            matricula = Matricula.objects.get(pk=pk)
            matricula.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Matricula.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        matricula = Matricula.objects.get(pk=pk)
        serializer = MatriculaSerializer(matricula)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        matricula = Matricula.objects.get(pk=pk)
        serializer = MatriculaSerializer(matricula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        matricula = Matricula.objects.get(pk=pk)
        serializer = MatriculaSerializer(matricula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        matricula = Matricula.objects.get(pk=pk)
        matricula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
