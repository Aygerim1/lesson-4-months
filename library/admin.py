from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate']
    list_filter = ['rate', ]
    search_fields = ['title', ]


admin.site.register(Category)
admin.site.register(Tag)