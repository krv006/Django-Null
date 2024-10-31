from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, IntegerField, Manager, ForeignKey, CASCADE, AutoField, BigIntegerField, \
    BinaryField, DurationField, SmallIntegerField, FilePathField, GeneratedField, GenericIPAddressField, \
    PositiveBigIntegerField, PositiveSmallIntegerField, SmallAutoField, Index
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

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


botir_username = RegexValidator(
    regex=r'^(?!.*botir).*$',
    message="Botir bolsang kira olmaysan!"
)


class User(AbstractUser):
    username = CharField(
        max_length=150,
        unique=True,
        validators=[botir_username],
        help_text="botir bolsang kira olmaysan",
        error_messages={
            'unique': "Ushbu foydalanuvchi nomi allaqachon foydalanilmoqda.",
        },
    )

    def save(self, *args, **kwargs):
        if "botir" in self.username.lower():
            raise ValidationError("Botir bolsang kira olmaysan")
        return super().save(*args, **kwargs)

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


class Section(Model):
    name = CharField(max_length=255)
    b = BigIntegerField()  # todo big number save
    c = BinaryField()  # todo two info save
    d = DurationField()  # todo time save "vaqt davomida saqlash"
    e = SmallIntegerField()  # todo small number
    # f = FilePathField(path="/rv/")  # todo road to file path=""
    h = GenericIPAddressField()  # todo Ipv4 Ipv6
    i = PositiveBigIntegerField()  # todo + Number
    j = PositiveSmallIntegerField()  # todo - Number
    k = SmallAutoField(primary_key=True)  # todo auto small Number create


class Customer(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)

    class Meta:
        indexes = [
            Index(fields=["last_name", "first_name"]),
            Index(fields=["first_name"], name="first_name_idx"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
