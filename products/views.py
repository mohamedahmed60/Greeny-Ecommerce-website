from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductImages ,Brand
from django.db.models import Count
# Create your views here.

class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context["images"] = ProductImages.objects.filter(product=myproduct)
        context['related'] = Product.objects.filter(category=myproduct.category)[:10]
        return context

class BrandList(ListView):
    model = Brand



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context
