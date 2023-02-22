from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductImages , Brand , Category
from django.db.models import Count , Q , F # F لاستعمل العمود نستخدم  Q,لاستخدام الاستعلامات
# Create your views here.

def post_list(request):
    # price_lte=30 اصغر من او يساوي,price_lt=30 اصغرمن , price__gte=30 اكبر من او يساوي ,price__gt=30 اكبر من
    # objects = Product.objects.all()
    # objects = Product.objects.filter(price__range=(30,50))
    # objects = Product.objects.filter(price__range=(30,50))
    # objects = Product.objects.filter(category__id=10)
    # objects = Product.objects.filter(category__id__gt=10)
    # objects = Product.objects.filter(name__startswith='S')
    # objects = Product.objects.filter(name__endswith='e')
    # objects = Product.objects.filter(desc__isnull=True)
    # objects = Product.objects.filter(desc__isnull=True)
    # objects = Product.objects.filter(quantity__gt=10)

    # objects = Product.objects.filter(quantity__gt=10, price__gt=50)
    # # عند استخدام الكويري
    # objects = Product.objects.filter(
    #     Q(quantity__gt=10) & # | or & and ~ not equl
    #     ~Q(price__gt=50)
    # )

    # objects = Product.objects.filter(quantity=F('price')) # عند المقارنه بين عمودين
    # objects = Product.objects.filter(quantity=F('category__id'))
    # objects = Product.objects.order_by('name')
    # objects = Product.objects.order_by('-name')
    # objects = Product.objects.order_by('name','-price')
    # objects = Product.objects.filter(quantity=F('price')).order_by('-name')
    # لجلب عناصر محدده
    # objects = Product.objects.all().order_by('-name')[:10]
    # لجلب اول عنصر فقط first earliest end latest
    # objects = Product.objects.latest('name')
    # objects = Product.objects.all()[10:20]
    # data___Dectionary recovery
    # objects = Product.objects.values('id','name','category__name')
    # data___typle recovery
    # objects = Product.objects.values_list('id','name','category__name','brand')
    # objects = Product.objects.only('id','name')

    objects = Product.objects.select_related('category').all() # one to one use select_related foreignkey
    objects = Product.objects.prefetch_related('category').all() # many to many use prefetch_related


    print(objects)


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

