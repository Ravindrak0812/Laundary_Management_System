# laundry/admin.py
from django.contrib import admin
from .models import Customer, LaundryItem, LaundryOrder, OrderItem, Payment, Delivery, LaundryEmployee, Inventory

admin.site.register(Customer)
admin.site.register(LaundryItem)
admin.site.register(LaundryOrder)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(LaundryEmployee)
admin.site.register(Inventory)
