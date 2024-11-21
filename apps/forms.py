# from django.contrib.admin.forms import AdminAuthenticationForm
# from django.core.exceptions import ValidationError
#
#
# class CustomAdminAuthenticationForm(AdminAuthenticationForm):
#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         if "botir" in username.lower():
#             raise ValidationError("Botir bo'lsang kira olmaysan")
#         return username
#
#
# def botir_username(value):
#     if 'botir' in value.lower():
#         raise ValidationError("Foydalanuvchi nomida 'botir' so'zi bo'lishi mumkin emas.")
