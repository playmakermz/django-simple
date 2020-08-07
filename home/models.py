from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    penjelasan = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    myfile = models.FileField(upload_to='file/%w')

    def __str__(self):
        return self.title