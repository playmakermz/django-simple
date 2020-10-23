from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    tipe = models.CharField(max_length=100)
    ukuran = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    myfile = models.FileField(upload_to='file/%w')

    def __str__(self):
        return self.title
