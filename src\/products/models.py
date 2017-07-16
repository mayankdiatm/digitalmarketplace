from django.db import models

# Create your models here.
class Product(models.Model):
    """docstring for ."""
    title = models.CharField(max_length=128)
    description = models.TextField(default="True")
    price = models.DecimalField(max_digits=10, decimal_places=2,default=9.99)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2,default=6.99,null=True,blank=True)


    def __unicode__(self):
        return self.title
