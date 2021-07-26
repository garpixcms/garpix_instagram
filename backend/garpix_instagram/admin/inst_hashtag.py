from django.contrib import admin
from ..models.inst_hashtag import InstagramHashtag


@admin.register(InstagramHashtag)
class InstagramHashtagAdmin(admin.ModelAdmin):
    pass
