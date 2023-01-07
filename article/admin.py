from django.contrib import admin
from .models import Article, Like,SendMailMessage

# Register your models here.
admin.site.register(Like)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date']
    list_display_links = ['title', 'author']
    search_fields = ['title']
    list_filter = ['created_date']

    class Meta:
        model = Article
        
        
@admin.register(SendMailMessage)
class SendMailMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail_address']
    list_display_links = ['name', 'mail_address']
    search_fields = ['mail_address']
    list_filter = ['mail_address']

    class Meta:
        model = SendMailMessage
