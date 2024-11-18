# Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline="Hello")

import os
from itertools import product
from ssl import create_default_context
from traceback import print_tb
from venv import create

import django
from django.db import transaction
from django.db.models import Count, Q, F

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

from apps.models import Product

# p = Product.objects.get(id=1)
# print(p)

# p = Product.objects.create(name='Kamron')
# print(p)

# p = Product.objects.get_or_create(name='Rustamov')
# print(p)

# p = Product.objects.latest('price')
# print(p)

# p = Product.objects.aggregate(Count('price'))
# print(p)

# p = Product.objects.select_for_update().filter(category_id=1)
# with transaction.atomic():
#     for i in p:
#         print(i.name)


# obj, created = Product.objects.get_or_create(
#     name='rv',
#     # defaults={'name':'rv'}
# )

# obj, updated = Product.objects.update_or_create(
#     name='rv',
#     defaults={'name' : 'salomas'}
# )

# todo aynan qaysidir ustunga narsa qoshadi qoganiga qoshmaydi
# objs = Product.objects.bulk_create(
#     [Product(description='Hiasa')],
#     [Product(description='Hiasa')],
#     [Product(description='Hiasa')],
#     [Product(description='Hiasa')],
#     [Product(description='Hiasa')]
#     , batch_size=2) # todo database ga 3 ta query boradi 2 ta 2 tadan bolib xammasni


# objs = [
#     Product.objects.create(description="salm")
# ]
# Product.objects.bulk_update(objs, ["description"])

# p = Product.objects.count('name')
# p = Product.objects.filter(category_id=1).count()
# print(p)

# p = Product.objects.distinct("name").in_bulk(['banan', 'apple'], field_name="name")
# # p = Product.objects.in_bulk(['name'])
# print(p)

# todo task 1
# p = Product.objects.filter(
#     Q(category__name__icontains='meva') | Q(name='banan')
# ).update(price=25000)
# print(p)

# todo task 2
# p = Product.objects.filter(category__name__icontains='meva').update(price=F("price") * 2)
# print(p)
# print(Product.objects.filter(name='banan').count())
# print(Product.objects.filter(name='banan'))

# product = Product.objects.earliest('name', 'price')
# print(product.id, product.name)
# todo ikkalasi xam bir xil ishlaydi
# product = Product.objects.order_by('name', 'price').first()
# print(product.id, product.name)

# for product in products:
#     print(product)


# products = Product.objects.filter(name='banan').iterator()
#
# for product in products:
#     print(product)


# d = {
#     'key' : 'vali1',
#     'key' : 'alijon',
# }
# print(d['key'])

# p = Product.objects.in_bulk(['banan', 'apple'], field_name='name')
# print(p)

# todo polars, numpy, pandas -> agar komp 4gb bolsa
#   mana shular orqali 20gb li narsani bolib bolib ochb olsa boladi
