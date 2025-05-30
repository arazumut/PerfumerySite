from django.contrib import admin
from .models import Category, Product, UserProfile, WishList, Cart, CartItem, Order, OrderItem, Blog

# Admin panel configurations
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    date_hierarchy = 'created_at'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_available', 'is_featured', 'is_new', 'created_at')
    list_filter = ('is_available', 'is_featured', 'is_new', 'category')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'country')
    search_fields = ('user__username', 'user__email', 'phone', 'city', 'country')

class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'product__name')
    date_hierarchy = 'created_at'

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__username',)
    inlines = [CartItemInline]
    date_hierarchy = 'created_at'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'first_name', 'last_name', 'email')
    inlines = [OrderItemInline]
    date_hierarchy = 'created_at'

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
    date_hierarchy = 'created_at'

# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Blog, BlogAdmin)
