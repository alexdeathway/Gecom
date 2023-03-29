from django.contrib import admin

from games.models import (
                    GamesModel,
                    OrganisationModel,
                    CategoryModel,
                    BoughtModel,
                    GameImageModel,
                    )

# Register your models here.
admin.site.register(GamesModel)
admin.site.register(OrganisationModel)
admin.site.register(CategoryModel)
admin.site.register(BoughtModel)
admin.site.register(GameImageModel)