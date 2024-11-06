import uuid
from datetime import datetime

import pytz
from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import CharField, Model, ForeignKey, CASCADE, UUIDField, DateTimeField, TimeField, DurationField, \
    ImageField, PositiveIntegerField
from django.utils import timezone

# from apps.forms import botir_username


#
# class BaseMetaMixin:
#     class Meta:
#         verbose_name = 'Mahsulot'
#         db_tablespace = 'valijon_tablespace'
#
#
# class Product(Model):
#     name = CharField(max_length=100, db_tablespace="valijon_tablespace")
#     passport_series = CharField(max_length=2, null=True)
#     passport_number = CharField(max_length=7, null=True)
#
#     def __str__(self):
#         return f"{self.id} - {self.name}"
#
#     class Meta(BaseMetaMixin.Meta):
#         pass
#         # app_label = 'apps'
#         # abstract = True
#         # proxy = True
#         # db_table = 'apps_product'
#         # verbose_name_plural = 'Products'
#         # unique_together = [
#         #     ('passport_series', 'passport_number')
#         # ]
#         # indexes = [
#         #     Index(fields=['name'], name='name'),
#         # ]
#         # ordering = ['-name']
#         # db_table = 'category'
#         # db_table_comment = "Question answers"
#
#
# class KamronManager(Manager):
#
#     def get_queryset(self):
#         return super().get_queryset().filter(name__icontains='kamron')
#
#
# class Category(Model):
#     name = CharField(max_length=255, db_comment='Bu ismi kiritadigan joy')
#     price = IntegerField(db_default=1000)
#     kamron = KamronManager()
#     ikkinchi = Manager()
#
#     def __str__(self):
#         return f"{self.id} - {self.price}"
#
#     class Meta(BaseMetaMixin):
#         verbose_name_plural = 'Categories'
#         default_manager_name = 'ikkinchi'
#
#
# class BookCategory(Model):
#     name = CharField(max_length=255)
#
#
# class Book(Model):
#     name = CharField(max_length=255)
#     category = ForeignKey('apps.BookCategory', CASCADE)
#
#     # class Meta:
#     #     default_related_name = 'valijonni_boglanishi'
#

# category.valijonni_boglanishi.all()
# category.book_set.all()
# category.vali.all()


# botir_username = RegexValidator(
#     regex=r'^(?!.*botir).*$',
#     message="Botir bolsang kira olmaysan!"
# )
#
#
# class User(AbstractUser):
#     username = CharField(
#         max_length=150,
#         unique=True,
#         validators=[botir_username],
#         help_text="botir bolsang kira olmaysan",
#         error_messages={
#             'unique': "Ushbu foydalanuvchi nomi allaqachon foydalanilmoqda.",
#         },
#     )
#
#     def save(self, *args, **kwargs):
#         if "botir" in self.username.lower():
#             raise ValidationError("Botir bolsang kira olmaysan")
#         return super().save(*args, **kwargs)

# def clean(self):
#     super().clean()
#     username = self.cleaned_data.get("username")
#     if username and "botir" in username.lower():
#         raise ValidationError("Botir bo'lsang kira olmaysan")
#     return self.cleaned_data

# def clean_username(self):
#     username = self.cleaned_data.get('username')
#     if 'botir' in username.lower():
#         raise ValidationError("Foydalanuvchi nomida 'botir' so'zi bo'lishi mumkin emas.")
#     username_digits_only = re.sub(r'[^\d]', '', username)
#     if len(username_digits_only) < 9:
#         return username_digits_only
#     return username_digits_only[-9:]


# class Section(Model):
#     name = CharField(max_length=255)
#     b = BigIntegerField()  # todo big number save
#     c = BinaryField()  # todo two info save
#     d = DurationField()  # todo time save "vaqt davomida saqlash"
#     e = SmallIntegerField()  # todo small number
#     # f = FilePathField(path="/rv/")  # todo road to file path=""
#     h = GenericIPAddressField()  # todo Ipv4 Ipv6
#     i = PositiveBigIntegerField()  # todo + Number
#     j = PositiveSmallIntegerField()  # todo - Number
#     k = SmallAutoField(primary_key=True)  # todo auto small Number create
#
#
# class Customer(Model):
#     first_name = CharField(max_length=100)
#     last_name = CharField(max_length=100)
#     age = IntegerField()
#
#     class Meta:
#         indexes = [
#             Index(fields=["last_name", "first_name"]),
#             Index(fields=["first_name"], name="first_name_idx"),
#             CheckConstraint(condition=Q(age__gte=18), name="age_gte_18"),
#         ]
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# def get_tashkent_time():
#     return timezone.now().astimezone(pytz.timezone('Asia/Tashkent'))
#
#
# def get_current_time_utc_plus_5():
#     # UTC vaqtini olish
#     utc_now = timezone.now()
#     # UTC+5 ga o'zgartirish
#     utc_plus_5 = utc_now.astimezone(pytz.timezone('Etc/GMT-5'))
#     return utc_plus_5
#
#
# class Category(Model):
#     uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = CharField(max_length=255)
#     created_at = DateTimeField(auto_now_add=True)
#
#
# class Product(Model):
#     uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = CharField(max_length=255)
#     category = ForeignKey("apps.Category", on_delete=CASCADE)
#     times = DateTimeField(default=timezone.localtime(get_tashkent_time()))
#     # timezone.localtime(utc_time_on_db)

# class Product(Model):
#     model = DurationField(null=True, blank=True)
#     photo = ImageField(null=True, blank=True)  # todo Image di delete qilish
#
#     def delete(self, using=None, keep_parents=False):
#         self.photo.delete(save=False)
#         return super().delete(using, keep_parents)


# get_user_model()
#
#
# class A(Model):
#     name = CharField(max_length=255, unique=True)
#
#
# class B(Model):
#     name = CharField(max_length=255, unique=True)
#
#
# class C(Model):
#     name = CharField(max_length=255, unique=True)
#
#
# class D(Model):
#     name = CharField(max_length=255, unique=True)
#
#
# class Image(Model):
#     image = ImageField(upload_to='images')
#     content_type = ForeignKey('contenttypes.ContentType', on_delete=CASCADE)
#     object_id = PositiveIntegerField()
#     content_object = GenericForeignKey('contenttypes.ContentType', 'object_id')


class Hi(Model):
    pass