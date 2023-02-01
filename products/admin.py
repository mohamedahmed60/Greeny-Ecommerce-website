from django.contrib import admin

# Register your models here.
from .models import Product , ProductImages , ProductReview , Category , Brand


class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'flag']
    inlines = [ProductImagesInline]


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
admin.site.register(Category)
admin.site.register(Brand)

