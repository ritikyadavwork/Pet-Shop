from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from classbasedview.ecom.forms import ProductForm
from classbasedview.ecom.models import Product, Category


class ProductAddView(CreateView):
    model = Product
    template_name = 'product/_form.html'
    form_class = ProductForm

    def get_success_url(self):
        messages.success(self.request, 'Product added successfully !!')
        return reverse('ecom:product_list')


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.filter(is_active=True)
        return context
