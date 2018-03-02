from django.contrib import admin
from cl_goods.models import GoodInfo, TypeInfo,GoodImage
# Register your models here.
admin.site.register(TypeInfo)
admin.site.register(GoodInfo)
admin.site.register(GoodImage)
