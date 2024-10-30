from django.contrib import admin

from apps.models import Section, User
from .forms import CustomAdminAuthenticationForm

admin.AdminSite.login_form = CustomAdminAuthenticationForm
admin.site.register(User)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
