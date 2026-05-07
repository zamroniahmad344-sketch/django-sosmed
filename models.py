from django.db import models

# Create your models here.
class Instagram(models.Model):
    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def _str_(self):
        return "{}.{}".format(*args:self.id, self.username)