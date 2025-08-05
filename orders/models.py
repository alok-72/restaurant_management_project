from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length = 20, unique=True)
    customer_name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    total_order = models.FloatField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order_id} by {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related='items')
    item_name = models.CharField(max_length=100)
    item_price = models.FloatField()
    qnty = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.qnty} x {self.item_name}"

