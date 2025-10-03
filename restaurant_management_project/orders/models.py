from django.db import models
from customers.models import Customer
from menu.models import Item
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    def total_price(self):
        return sum(oi.item.price * oi.quantity for oi in self.items.all())
    def __str__(self):
        return f'Order #{self.id} - {self.customer.name}'
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.quantity} x {self.item.name}'
