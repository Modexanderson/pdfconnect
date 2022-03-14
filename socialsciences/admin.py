from django.contrib import admin
from .models import Book
# Register your models here.


class SocialSciencesAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'pdf', 'cover', 'description')


admin.site.register(Book, SocialSciencesAdmin)
