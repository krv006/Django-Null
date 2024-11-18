# import os
#
# import django
# from django.db.models import Q, F, Avg, Count, OrderBy, Value, CharField
# from django.db.models.functions import Upper, Concat, Cast
# from django.shortcuts import get_object_or_404
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
#
# django.setup()
#
# from apps.models import Product, Category
#
# product_id = input('Product id: ')
#
# products = Product.objects.raw("select * from apps_product where id = %s" % product_id).using('valijon')
# # products = Product.objects.raw("select * from apps_product where id = %s", [product_id])
#
# for i in products:
#     print(i)
