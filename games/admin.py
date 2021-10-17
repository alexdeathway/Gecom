from django.contrib import admin

from games.models import (
                    GamesModel,
                    PublisherModel,
                    CategoryModel,
                    BoughtModel,
                    )

# Register your models here.
admin.site.register(GamesModel)
admin.site.register(PublisherModel)
admin.site.register(CategoryModel)
admin.site.register(BoughtModel)