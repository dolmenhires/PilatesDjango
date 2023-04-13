"""pilates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers

from alumnos.views import AlumnosSearchListView, AlumnosDetailView
from actividades.views import ActividadesSearchListView, ActividadesDetailView
from matriculas.views import MatriculasSearchListView, MatriculasDetailView
from profesores.views import ProfesoresSearchListView, ProfesoresDetailView
from clases.views import ClasesSearchListView, ClasesDetailView

router = routers.DefaultRouter()

router.register('alumnos/list', AlumnosSearchListView, basename='alumnos_list')
router.register('alumnos/detail', AlumnosDetailView, basename='alumnos_detail')
router.register('actividades/list', ActividadesSearchListView, basename='actividades_list')
router.register('actividades/detail', ActividadesDetailView, basename='actividades_detail')
router.register('matriculas/list', MatriculasSearchListView, basename='matriculas_list')
router.register('matriculas/detail', MatriculasDetailView, basename='matriculas_detail')
router.register('profesores/list', ProfesoresSearchListView, basename='profesores_list')
router.register('profesores/detail', ProfesoresDetailView, basename='profesores_detail')
router.register('clases/list', ClasesSearchListView, basename='clases_list')
router.register('clases/detail', ClasesDetailView, basename='clases_detail')

urlpatterns = [
    url('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
