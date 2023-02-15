from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductImages , Brand , Category
from django.db.models import Count
# Create your views here.

def post_list(request):
    # price_lte=30 اصغر من او يساوي,price_lt=30 اصغرمن , price__gte=30 اكبر من او يساوي ,price__gt=30 اكبر من
    # objects = Product.objects.filter(price__range=(30,50))
    objects = Product.objects.filter(price__range=(30,50))
    return render(request, 'products/test_list.html',{'products':objects})


class ProductList(ListView):
    model = Product
    paginate_by = 100 #الصفحة المعروضة


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
    # paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context



class BrandDetail(DetailView):
    model = Brand


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context


class CategoryList(ListView):
    model = Category
    # paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all().annotate(product_count=Count('product_category'))
        return context

