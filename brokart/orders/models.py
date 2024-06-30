from django.db import models
from customers.models import Customer  # Ensure correct import for Customer model
from products.models import Product  # Ensure correct import for Product model

# MODEL FOR ORDER
class Order(models.Model):  # Correct base class to models.Model
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')  # Correct ForeignKey and related_name
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.owner.name}"

# MODEL FOR ORDERED ITEM
class OrderedItem(models.Model):  # Correct base class to models.Model
    product = models.ForeignKey(Product, related_name='added_items', null=True, on_delete=models.SET_NULL)  # Correct ForeignKey and related_name
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')  # Correct ForeignKey and related_name

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order #{self.order.pk}"
