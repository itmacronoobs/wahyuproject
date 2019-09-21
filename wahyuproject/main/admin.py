from django.contrib import admin


# Register your models here.
from .models import ship2, Orders, Products, Category, Subcategory, Discounts, Distributors, Reviews, Tag, Blog, Customers

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Discounts)
admin.site.register(Distributors)
admin.site.register(Reviews)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Customers)
admin.site.register(ship2)
admin.site.register(Orders)