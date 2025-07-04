from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class MyBooks(models.Model):
    title = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    def __str__(self):
        return self.title
