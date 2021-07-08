from django.contrib import admin
from .models import Book
# Register your models here.


class EngineeringAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'pdf', 'cover')


admin.site.register(Book, EngineeringAdmin)
