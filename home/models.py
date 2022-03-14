# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     pdf = models.FileField(upload_to='books/pdfs/')
#     cover = models.ImageField(upload_to='photos/')
#     description = models.TextField()

#     def delete(self, using=None, keep_parents=False):
#         self.modelling_photo.storage.delete(self.modelling_photo.name)
#         super().delete()

#     def __str__(self):
#         return self.title
