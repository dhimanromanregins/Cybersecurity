from django.contrib import admin
from .models import ProductTags, Products, ProductCategory, ProductReview
# Register your models here.
admin.site.register(Products)
admin.site.register(ProductCategory)
admin.site.register(ProductTags)
admin.site.register(ProductReview)
