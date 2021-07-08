from django.contrib import admin
from .models import Book
# Register your models here.


class EnviromentalSciencesAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'pdf', 'cover')


admin.site.register(Book, EnviromentalSciencesAdmin)
