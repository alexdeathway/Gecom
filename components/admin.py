from django.contrib import admin
from .models import ComponentCategoryModel, ComponentsModel
# Register your models here.
admin.site.register(ComponentCategoryModel)
admin.site.register(ComponentsModel)

