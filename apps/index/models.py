from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='book_creator')
    title = models.CharField(max_length=100, verbose_name='Título')
    image = models.ImageField(upload_to='static/assets/img/books/', null=True, verbose_name='Imagen')
    description = models.TextField(null=True, verbose_name='Descripción')
    creation_date = models.DateField(auto_now=True, verbose_name='Fecha de creación')
    status = models.BooleanField(default=False, verbose_name='Estado')

    # class Meta:
    #     verbose_name = 'Book'
    #     verbose_name_plural = 'Books'
    #     ordering = ['title']

    def __str__(self):
        return (f'{self.id} - {self.title} - {self.creator}')

    def delete(self, using=None, keep_parents=False): # Borra la imagen cuando se borra el registro del libro
        self.image.storage.delete(self.image.name)
        super().delete()