from django.db import models
from django.core.validators import FileExtensionValidator

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/', validators=[FileExtensionValidator(['pdf', 'docx', 'pptx', 'doc', 'txt', 'ppt', 'epub', 'pps', ])])
    description = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
