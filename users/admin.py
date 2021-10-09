from django.contrib import admin
from .models import User,PublisherModel

# Register your models here.
admin.site.register(User)
admin.site.register(PublisherModel)
