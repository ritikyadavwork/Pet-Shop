from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from classbasedview.ecom.forms import ProductForm
from classbasedview.ecom.models import Product


class ProductAddView(CreateView):
    model = Product
    template_name = 'product/_form.html'
    form_class = ProductForm

    def get_success_url(self):
        messages.success(self.request, 'Product added successfully !!')


class ProductListView(ListView):
    model = Product
    template_name =''
