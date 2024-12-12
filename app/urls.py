from django.urls import path

from .views import index, municipio, ouvidoria, esic, ex_presidentes, ProjetosDeLeiView

urlpatterns = [
    path("", index, name="index"),
    path("municipio/", municipio, name="municipio"),
    path("ouvidoria/", ouvidoria, name="ouvidoria"),
    path("esic/", esic, name="esic"),
    path("ex-presidentes/", ex_presidentes, name="ex-presidentes"),
    path("projetos-de-lei/", ProjetosDeLeiView.as_view(), name="projetos-de-lei"),
]
