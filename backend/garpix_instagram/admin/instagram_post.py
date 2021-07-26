from django.contrib import admin
from ..models.instagram_post import InstagramPost


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    pass
