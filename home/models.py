from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    suara = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title