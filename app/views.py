from django.views.generic import ListView
from django.shortcuts import render
from .models import ProjetoDeLei, ExPresidente


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


class ExPresidentesView(ListView):
    model = ExPresidente
    template_name = "app/ex-presidentes.html"
    context_object_name = "object_list"
    paginate_by = 3


class ProjetosDeLeiView(ListView):
    model = ProjetoDeLei
    template_name = "app/projetos-de-lei.html"
    context_object_name = "object_list"
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        ano = self.request.GET.get("ano")

        if search:
            queryset = queryset.filter(numero__icontains=search) | queryset.filter(
                descricao__icontains=search
            )

        if ano:
            queryset = queryset.filter(ano=int(ano))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["anos"] = ["2021", "2022", "2023", "2024"]
        context["search"] = self.request.GET.get("search", "")
        context["ano_selected"] = self.request.GET.get("ano")
        return context
