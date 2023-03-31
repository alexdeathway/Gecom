from django.contrib import admin

from games.models import (
                    GamesModel,
                    OrganisationModel,
                    CategoryModel,
                    CartItemModel,
                    GameImageModel,
                    )

# Register your models here.
admin.site.register(GamesModel)
admin.site.register(OrganisationModel)
admin.site.register(CategoryModel)
admin.site.register(CartItemModel)
admin.site.register(GameImageModel)