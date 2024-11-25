from django.contrib import admin
from django.db import connections
from apps.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.save()
        with connections['second_db'].cursor() as cursor:
            cursor.execute("INSERT INTO apps_product(name, price) VALUES (%s, %s);", [obj.name, obj.price])


# from apps.models import Category, Product
#
#
# # from apps.models import History
#
#
# # from apps.models import History
#
#
# # from apps.models import Product
# #
# # # from apps.models import Category, Product
# #
# # # from apps.models import Section, User, Customer
# # # from .forms import CustomAdminAuthenticationForm
# # #
# # # admin.AdminSite.login_form = CustomAdminAuthenticationForm
# # # admin.site.register(Category)
# # admin.site.register(Product)
# # #
# # #
# # # @admin.register(Section)
# # # class SectionAdmin(admin.ModelAdmin):
# # #     pass
# # #
# # #
# # @admin.register(Customer)
# # class CustomerAdmin(admin.ModelAdmin):
# #     pass
#
#
# # @admin.register(Category)
# # class CategoryAdmin(ModelAdmin):
# #     exclude = ('slug',)
# #     list_display = ('name', 'uuid', 'slug')
# #
# #
# # @admin.register(Product)
# # class ProductAdmin(ModelAdmin):
# #     list_display = ('name', 'category_id', 'category_uuid', 'category_slug')
#
# #
# # @admin.register(History)
# # class HistoryAdmin(admin.ModelAdmin):
# #     pass
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     # def get_queryset(self, request):
#     #     qs = super().get_queryset(request)
#     #
#     #     return qs
#     pass
#
#     # products = Product.objects.select_related('category').all()
#     #
#     # for product in products:
#     #     print(f"Mahsulot: {product.name}, Kategoriya: {product.category.name}")
