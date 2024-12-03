from django.contrib import admin
from .models import Item, Order, OrderItem  # Fixed import path

# Admin customization for Item model
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # Fixed spacing and tuple syntax
    list_display = [
        'title',
        'price',
        'discount',  # Changed 'discount_price' to 'discount' (to match model field name)
    ]

# Register models with the admin site
admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)