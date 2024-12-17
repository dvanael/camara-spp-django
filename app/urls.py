from django.urls import path

from .views import (
    index,
    municipio,
    ouvidoria,
    esic,
    ExPresidentesView,
    ProjetosDeLeiView,
    search_pages,
    erro_404,
    erro_500,
)

urlpatterns = [
    path("", index, name="index"),
    path("municipio/", municipio, name="municipio"),
    path("ouvidoria/", ouvidoria, name="ouvidoria"),
    path("esic/", esic, name="esic"),
    path("ex-presidentes/", ExPresidentesView.as_view(), name="ex-presidentes"),
    path("projetos-de-lei/", ProjetosDeLeiView.as_view(), name="projetos-de-lei"),
    path("search/", search_pages, name="search"),
    # test erro
    path("404/", erro_404, name="404"),
    path("500/", erro_500, name="500"),
]
