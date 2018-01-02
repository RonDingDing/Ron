from django.contrib import admin
from . models import Article
# Register your models here.
# admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter =('pub_time', )

admin.site.register(Article, ArticleAdmin)
