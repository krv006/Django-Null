# Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline="Hello")

import os
from audioop import reverse
from datetime import datetime
from itertools import count, product

import django
from django.db.models import Count, Value
from django.db.models.functions import ExtractMonth

from sql import products

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

from apps.models import Product, Category

# for i in Product.objects.filter(created_at_month=11):
#     print(i)
#
# for i in Product.objects.exclude(created_at__month=10):
#     print(i)
#
# for i in Product.objects.annotate(created_at_month=ExtractMonth('created_at')).filter(created_at_month=11):
#     print(i)
#
# for i in Product.objects.alias(Count('name')):
#     print(i)
#
# for i in Product.objects.alias(created_at_month=ExtractMonth('created_at')).filter(created_at_month=11):
#     print(i) # todo aqtinchalik hisoblangan ustunlarni qo‘shish uchun qulay usuldir.
#
# products = Product.objects.order_by('price')
# print(products)
#
# products = Product.objects.order_by('price').reverse()
# print(products)
#
# products = Product.objects.order_by('created_at')[:5]  # O'sish tartibida saralaydi
# products_reversed = products.reverse()  # Natijalarni teskari qilib o'zgartiradi
# print(products_reversed)
#
# todo reverse() bu order_by di teskari qilib beradi
#
#
# products = Product.objects.order_by('price')
# products = products.extra(select={'null_check': 'price IS NULL'}, order_by=['null_check', '-price'])
#
# for product in products:
#     print(product.price)
#
# for i in Product.objects.order_by('name'):
#     print(i)
#
# for i in Category.objects.all():
#     print("category-> ", i)
#
# for i in Product.objects.all():
#     print("product-> ", i)
#
#
# categories = Category.objects.filter(name__icontains="texnika").values("name").annotate(type=Value("Category"))
#
# products = Product.objects.filter(name__icontains="texnika").values("name").annotate(type=Value("Product"))
#
# s = categories.union(products)
#
# for item in s:
#     print(f"{item['name']} - {item['type']}") # todo product va category filter name ikkalasda xam bir xil name borligini chiqazish
#
#
# products = Product.objects.extra(where=["price > 1200000"])
# for product in products:
#     print(product.name, product.price)
#
# products = Product.objects.extra(order_by=['-price'])
# for product in products:
#     print(product.price)
#
# products = Product.objects.only('name', 'price')
# for product in products:
#     print(f"{product.name} - {product.price}")
#
# # raw todo bunda postgres query yozsa boladi
# # defer todo yuklanmaydi
#
# products = Product.objects.defer('description')
# for product in products:
#     print(product.name)
#     print(product.description)
#
# raw di korib kelish kere buzish uchun kere boladi sayt lardi


p = Product.objects.get(id=1)
print(p)


