from django.contrib import admin
from .models import Book, Order

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'book_available')  # Columns shown in admin panel
    search_fields = ('title', 'author')  # Add search bar
    list_filter = ('book_available',)  # Filter by availability
    ordering = ('title',)  # Order books alphabetically

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'created')

# Register models only ONCE
admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)
