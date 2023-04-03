from django.contrib import admin
from checkout.models import (
                    CartGameItemModel,
                    CartComponentItemModel
                        )
admin.site.register(CartGameItemModel)
admin.site.register(CartComponentItemModel)