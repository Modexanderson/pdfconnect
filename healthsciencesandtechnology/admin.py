from django.contrib import admin
from .models import Book
# Register your models here.


class HealthSciencesAndTechnologyAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'pdf', 'cover')


admin.site.register(Book, HealthSciencesAndTechnologyAdmin)
