from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Category, Product, Cart, CartItem, WishList, UserProfile, Order, OrderItem, Blog
from .forms import UserProfileForm, OrderForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    # Son eklenen 3 ürünü getir
    new_products = Product.objects.filter(is_available=True).order_by('-created_at')[:3]
    # Öne çıkan ürünleri getir
    featured_products = Product.objects.filter(is_available=True, is_featured=True)[:3]
    # Tüm kategorileri getir
    categories = Category.objects.all()[:5]
    # Son blog yazılarını getir
    latest_blogs = Blog.objects.all()[:2]
    
    context = {
        'new_products': new_products,
        'featured_products': featured_products,
        'categories': categories,
        'latest_blogs': latest_blogs,
    }
    return render(request, 'index.html', context)

def home_cosmetic(request):
    featured_products = Product.objects.filter(is_available=True, is_featured=True)[:6]
    latest_blogs = Blog.objects.all()[:2]
    context = {
        'featured_products': featured_products,
        'latest_blogs': latest_blogs,
    }
    return render(request, 'index.html', context)

def shop(request):
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')
    
    products = Product.objects.filter(is_available=True)
    
    # Kategori filtresi
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Arama filtresi
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Sayfalama
    paginator = Paginator(products, 9)  # Sayfa başına 9 ürün
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    context = {
        'products': page_obj,
        'categories': categories,
        'search_query': search_query,
    }
    return render(request, 'shop.html', context)

def product(request):
    return render(request, 'product.html')

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, is_available=True)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    # İstek listesinde mi kontrol et
    in_wishlist = False
    if request.user.is_authenticated:
        in_wishlist = WishList.objects.filter(user=request.user, product=product).exists()
    
    context = {
        'product': product,
        'related_products': related_products,
        'in_wishlist': in_wishlist,
    }
    return render(request, 'product.html', context)

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, is_available=True)
    
    # Sayfalama
    paginator = Paginator(products, 9)  # Sayfa başına 9 ürün
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'products': page_obj
    }
    return render(request, 'shop.html', context)

def product_default(request):
    return render(request, 'product_default.html')

def blog_main(request):
    blogs = Blog.objects.all()
    
    # Sayfalama
    paginator = Paginator(blogs, 6)  # Sayfa başına 6 blog yazısı
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'blogs': page_obj,
    }
    return render(request, 'blog_main.html', context)

def blog_post(request, blog_slug=None):
    if blog_slug:
        blog = get_object_or_404(Blog, slug=blog_slug)
        recent_posts = Blog.objects.exclude(id=blog.id).order_by('-created_at')[:3]
        context = {
            'blog': blog,
            'recent_posts': recent_posts,
        }
    else:
        # Eğer slug verilmemişse, ilk blog yazısını göster
        try:
            blog = Blog.objects.first()
            recent_posts = Blog.objects.exclude(id=blog.id).order_by('-created_at')[:3]
            context = {
                'blog': blog,
                'recent_posts': recent_posts,
            }
        except Blog.DoesNotExist:
            context = {}
    
    return render(request, 'blog_post.html', context)

def blog_post_detail(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    recent_posts = Blog.objects.exclude(id=blog.id).order_by('-created_at')[:3]
    context = {
        'blog': blog,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog_post.html', context)

def blog_post_new(request):
    return render(request, 'blog_post_new.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            full_message = f"İsim: {name}\nE-posta: {email}\n\n{message}"
            
            # E-posta gönderme işlemi
            try:
                send_mail(
                    subject,
                    full_message,
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapacağız.')
                return redirect('contact')
            except:
                messages.error(request, 'Mesajınız gönderilirken bir hata oluştu. Lütfen daha sonra tekrar deneyin.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)

def shop_default(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    
    # Sayfalama
    paginator = Paginator(products, 9)  # Sayfa başına 9 ürün
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'products': page_obj,
        'categories': categories,
    }
    return render(request, 'shop_default.html', context)

def shop_grid(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    
    # Sayfalama
    paginator = Paginator(products, 12)  # Sayfa başına 12 ürün
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'products': page_obj,
        'categories': categories,
    }
    return render(request, 'shop_grid.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Kullanıcı profili oluştur
            UserProfile.objects.create(user=user)
            # Otomatik giriş yap
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Hesabınız başarıyla oluşturuldu!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    return render(request, 'login.html')

def reset_password(request):
    return render(request, 'reset_password.html')

def about(request):
    return render(request, 'about.html')

def page_typography(request):
    return render(request, 'page_typography.html')

@login_required
def profile(request):
    profile = UserProfile.objects.get_or_create(user=request.user)[0]
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }
    return render(request, 'profile.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Kullanıcının sepeti var mı, yoksa yeni oluştur
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Ürün sepette var mı kontrol et
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        # Ürün sepette yoksa, yeni ekle
        CartItem.objects.create(cart=cart, product=product, quantity=1)
    
    messages.success(request, f"{product.name} sepetinize eklendi.")
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    
    messages.success(request, f"{product_name} sepetinizden kaldırıldı.")
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, "Sepetiniz güncellendi.")
        else:
            cart_item.delete()
            messages.success(request, f"{cart_item.product.name} sepetinizden kaldırıldı.")
    
    return redirect('cart')

@login_required
def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
    except Cart.DoesNotExist:
        cart = None
        cart_items = []
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)

@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        
        if not cart_items:
            messages.error(request, "Sepetiniz boş, lütfen önce ürün ekleyin.")
            return redirect('shop')
        
    except Cart.DoesNotExist:
        messages.error(request, "Sepetiniz boş, lütfen önce ürün ekleyin.")
        return redirect('shop')
    
    profile = UserProfile.objects.get_or_create(user=request.user)[0]
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            
            # Sepetteki ürünleri siparişe ekle
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )
            
            # Sepeti temizle
            cart_items.delete()
            
            messages.success(request, "Siparişiniz başarıyla oluşturuldu.")
            return redirect('order_complete', order_id=order.id)
    else:
        # Formu kullanıcı bilgileriyle doldur
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'phone': profile.phone,
            'address': profile.address,
            'city': profile.city,
            'country': profile.country,
            'postal_code': profile.postal_code,
        }
        form = OrderForm(initial=initial_data)
    
    context = {
        'form': form,
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'checkout.html', context)

@login_required
def order_complete(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
    }
    return render(request, 'order_complete.html', context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
    }
    return render(request, 'order_detail.html', context)

@login_required
def wishlist(request):
    wishlist_items = WishList.objects.filter(user=request.user)
    
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # İstek listesinde zaten var mı kontrol et
    wishlist_item, created = WishList.objects.get_or_create(user=request.user, product=product)
    
    if created:
        messages.success(request, f"{product.name} istek listenize eklendi.")
    else:
        messages.info(request, f"{product.name} zaten istek listenizde bulunuyor.")
    
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(WishList, id=item_id, user=request.user)
    product_name = wishlist_item.product.name
    wishlist_item.delete()
    
    messages.success(request, f"{product_name} istek listenizden kaldırıldı.")
    return redirect('wishlist')
