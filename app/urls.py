from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("municipio/", views.municipio, name="municipio"),
    path("ouvidoria/", views.ouvidoria, name="ouvidoria"),
    path("esic/", views.esic, name="esic"),
    path("ex-presidentes/", views.ex_presidentes, name="ex-presidentes"),
    path("projetos-de-lei/", views.projetos_de_lei, name="projetos-de-lei"),
]
