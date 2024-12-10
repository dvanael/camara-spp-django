from django.shortcuts import render


# Create your views here.
def index(request):
    template = "index.html"
    return render(request, template)


def municipio(request):
    template = "app/municipio.html"
    return render(request, template)


def ouvidoria(request):
    template = "app/ouvidoria.html"
    return render(request, template)


def esic(request):
    template = "app/esic.html"
    return render(request, template)


def ex_presidentes(request):
    template = "app/ex-presidentes.html"
    return render(request, template)


def projetos_de_lei(request):
    template = "app/projetos-de-lei.html"
    return render(request, template)
