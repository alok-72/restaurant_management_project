from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    total_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def is_available(self, quantity):
        if quantity <= 0:
            return False
        return self.total_stock >= quantity