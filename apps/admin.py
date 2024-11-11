from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category, Product


# from apps.models import Product
#
# # from apps.models import Category, Product
#
# # from apps.models import Section, User, Customer
# # from .forms import CustomAdminAuthenticationForm
# #
# # admin.AdminSite.login_form = CustomAdminAuthenticationForm
# # admin.site.register(Category)
# admin.site.register(Product)
# #
# #
# # @admin.register(Section)
# # class SectionAdmin(admin.ModelAdmin):
# #     pass
# #
# #
# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'uuid', 'slug')


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'category_id', 'category_uuid', 'category_slug')
