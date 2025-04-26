from django.contrib import admin

# Register your models here.

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "publish_date")


admin.site.register(Article, ArticleAdmin)

from articles.models import Article, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "article")


admin.site.register(Comment, CommentAdmin)