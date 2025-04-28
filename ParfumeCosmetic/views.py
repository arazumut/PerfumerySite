from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def index(request):
    # Son eklenen 3 ürünü getir
    new_products = Product.objects.filter(is_available=True).order_by('-created_at')[:3]
    # Öne çıkan ürünleri getir
    featured_products = Product.objects.filter(is_available=True, is_featured=True)[:3]
    # Tüm kategorileri getir
    categories = Category.objects.all()[:5]
    
    context = {
        'new_products': new_products,
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def home_cosmetic(request):
    featured_products = Product.objects.filter(is_available=True, is_featured=True)[:6]
    context = {
        'featured_products': featured_products,
    }
    return render(request, 'index.html', context)

def shop(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop.html', context)

def product(request):
    return render(request, 'product.html')

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, is_available=True)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'product.html', context)

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, is_available=True)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop.html', context)

def product_default(request):
    return render(request, 'product_default.html')

def blog_main(request):
    return render(request, 'blog_main.html')

def blog_post(request):
    return render(request, 'blog_post.html')

def blog_post_new(request):
    return render(request, 'blog_post_new.html')

def contact(request):
    return render(request, 'contact.html')

def shop_default(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop_default.html', context)

def shop_grid(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop_grid.html', context)

def login_view(request):
    return render(request, 'login.html')

def reset_password(request):
    return render(request, 'reset_password.html')

def about(request):
    return render(request, 'about.html')

def page_typography(request):
    return render(request, 'page_typography.html')
