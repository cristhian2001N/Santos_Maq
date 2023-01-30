from django.shortcuts import render, redirect
# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import  ListView, CreateView,UpdateView,DeleteView
from maquinari.forms import MaquinariaForm
from maquinari.models import Maquinaria


class maquinariaListView(ListView):
    template_name = "list.html"
    model = Maquinaria
    form_class = MaquinariaForm
    context_object_name = 'maquinarias'

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(Descripcion__icontains=query)
        else:
            return self.model.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crear_url'] = 'crearmaquinaria/'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearMaquinaria(CreateView):
    model = Maquinaria
    template_name = "form.html"
    success_url = reverse_lazy('maquinaria')
    form_class = MaquinariaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'add'
        return context

class ActualizarMaquinaria(UpdateView):
    model = Maquinaria
    template_name = "form.html"
    success_url = reverse_lazy('maquinaria')
    form_class = MaquinariaForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['url_anterior'] = 'maquinaria'
        return context

class EliminarMaquinaria(DeleteView):
    model = Maquinaria
    template_name = "delete.html"
    success_url = reverse_lazy('maquinaria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['url_anterior'] = 'maquinaria'
        return context