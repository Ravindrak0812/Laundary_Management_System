from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.user.username  # Or self.user.first_name if preferred

class LaundryItem(models.Model):
    name = models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class LaundryOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # Total amount of the order
    status_choices = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default='pending')

    def __str__(self):
        return f"Order {self.id} for {self.customer.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(LaundryOrder, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(LaundryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    # To automatically calculate the total price whenever a new order item is saved
    def save(self, *args, **kwargs):
        self.total_price = self.item.price_per_unit * self.quantity
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.item.name} for Order {self.order.id}"

class Payment(models.Model):
    order = models.ForeignKey(LaundryOrder, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)  # Total payment amount
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method_choices = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('cash', 'Cash'),
        ('online', 'Online Payment'),
    ]
    payment_method = models.CharField(max_length=20, choices=payment_method_choices)
    payment_status_choices = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('pending', 'Pending'),
    ]
    payment_status = models.CharField(max_length=15, choices=payment_status_choices, default='pending')

    def __str__(self):
        return f"Payment for Order {self.order.id} ({self.payment_status})"

class Delivery(models.Model):
    order = models.OneToOneField(LaundryOrder, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(null=True, blank=True)
    delivery_notes = models.TextField(null=True, blank=True)  # Field for special delivery instructions
    delivery_status_choices = [
        ('not_delivered', 'Not Delivered'),
        ('delivered', 'Delivered'),
        ('in_transit', 'In Transit'),
    ]
    delivery_status = models.CharField(max_length=15, choices=delivery_status_choices, default='not_delivered')

    def __str__(self):
        return f"Delivery for Order {self.order.id} ({self.delivery_status})"

class LaundryEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [
        ('washer', 'Washer'),
        ('folding', 'Folding'),
        ('delivery', 'Delivery'),
        ('management', 'Management'),
    ]
    role = models.CharField(max_length=15, choices=role_choices)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
