from django.contrib import admin

from webapp.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'done_date')
    list_filter = ('id', 'description', 'status', 'done_date')
    search_fields = ('id', 'done_date', 'status')
    fields = ('description', 'status', 'done_date')
    readonly_fields = ('id', 'done_date')


admin.site.register(Article, ArticleAdmin)
