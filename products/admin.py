from django.contrib import admin
from .models import Product

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'stock')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, MemberAdmin)
    
    