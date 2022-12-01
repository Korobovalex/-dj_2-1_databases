from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(upload_to='phones/%Y/%m/%d', blank=True)
    release_date = models.DateField(auto_now_add=True)
    lte_exists = models.BooleanField(default=False, null=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

