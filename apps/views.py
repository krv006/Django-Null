# from unicodedata import category
#
# from django.forms import model_to_dict
# from django.http import JsonResponse
# from asgiref.sync import sync_to_async
#
# from apps.models import Product, Category
# from asgiref.sync import sync_to_async
#
#
# async def index(request):
#     product = await Product.objects.aget(id=request.GET.get('id'))
#     category = await sync_to_async(Category.objects.get)(id=product.category_id)
#     return JsonResponse({
#         "message": "Hello World",
#         "product": model_to_dict(product, fields=['id', 'name']),
#         'category': category.name
#     })
