from django.db import models

class gallery(models.Model):
    urls_link_0 = models.CharField(max_length=500)
    urls_link_1 = models.CharField(max_length=500)
    urls_link_2 = models.CharField(max_length=500)
    title       = models.CharField(max_length=300, blank=True)
    tanggal     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class barang_jual(models.Model):
    url_link    = models.CharField(max_length=500)
    title       = models.CharField(max_length=300)
#    harga       = models.DecimalField(max_digits=19,decimal_places=10)
    harga_barang= models.IntegerField()
    # maxsimal 1 milliar
    deskripsi   = models.TextField()
    tanggal     = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class about_us(models.Model):
    url_link_0  = models.CharField(max_length=500)
    url_link_1  = models.CharField(max_length=500)
    url_link_2  = models.CharField(max_length=500)
    url_link_3  = models.CharField(max_length=500)
    deskripsi   = models.TextField(default="ini adalah text default")
    title_1 = models.CharField(max_length=400, default="ini untuk image 1")
    title_2 = models.CharField(max_length=400, default="ini untuk image 2")
    title_3 = models.CharField(max_length=400, default="ini untuk image 3")

    def __str__(self):
        return "hanya boleh ada satu about-us"
