from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.

PRODUCT_FLAC = (
    ('New' , 'New'),
    ('Feature' , 'Feature'),
    ('Sale' , 'Sale')
)

class Product(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    sku = models.IntegerField(_('SKU'))
    subtitle = models.CharField(_('Subtitle'),max_length=300)
    desc = models.TextField(_('Description'),max_length=10000)
    flag = models.CharField(_('Flag'),max_length=10 , choices=PRODUCT_FLAC)
    price = models.FloatField(_('Price'))
    image = models.ImageField(upload_to='products')
    tags = TaggableManager()
    category = models.ForeignKey('Category' ,verbose_name=_('Category'), related_name='product_category',on_delete=models.SET_NULL , null=True,blank=True)
    brand = models.ForeignKey('Brand' , verbose_name=_('Brand') , related_name='product_brand',on_delete=models.SET_NULL , null=True,blank=True)
    video_url = models.URLField(null=True,blank=True)
    quantity = models.IntegerField(default=50)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product,verbose_name=_('Product'),related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_('Image'),upload_to='productimages')

    def __str__(slef):
        return str(slef.product)

class Category(models.Model):
    name = models.CharField(_('Name'),max_length=100 )
    image = models.ImageField(_('Image'),upload_to='category')

    def __str__ (self):
        return self.name

class Brand(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    image = models.ImageField(_('Image'),upload_to='brand')

    def __str__(slef):
        return slef.name

class ProductReview(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='product_review',on_delete=models.SET_NULL , null=True,blank=True)
    rate = models.IntegerField(verbose_name=_('Rate'))
    review = models.CharField(verbose_name=_('Review'),max_length=300)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(slef):
        return str(slef.product)