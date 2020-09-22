from django.db import models

class pesanan(models.Model):
    nama = models.CharField(max_length=100)
    pesanan = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class acc1(models.Model):
    nama = models.CharField(max_length=100)
    pesanan = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class acc2(models.Model):
    nama = models.CharField(max_length=100)
    pesanan = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class acc3(models.Model):
    nama = models.CharField(max_length=100)
    pesanan = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class acc4(models.Model):
    nama = models.CharField(max_length=100)
    pesanan = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
