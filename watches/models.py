from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="product/brand/")
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Brand"

class Watch(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    qty = models.IntegerField()
    description = models.CharField(max_length=1000)
    date_created = models.DateField(auto_now_add=True)
    main_image = models.ImageField(upload_to="product/watch/")
    
    @property
    def has_stock(self):
        return self.qty > 0

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Watch"

class WatchImage(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/watch/")

    def __str__(self):
        return self.watch.name
    
    class Meta:
        db_table = "WatchImage"
