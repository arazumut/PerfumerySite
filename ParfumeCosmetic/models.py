from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Kategori URL")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Kategori Resmi")
    description = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Kategori")
    name = models.CharField(max_length=200, verbose_name="Ürün Adı")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Ürün URL")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Ürün Resmi")
    description = models.TextField(blank=True, verbose_name="Açıklama")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Eski Fiyat")
    is_available = models.BooleanField(default=True, verbose_name="Stokta Var Mı?")
    is_featured = models.BooleanField(default=False, verbose_name="Öne Çıkan Ürün Mü?")
    is_new = models.BooleanField(default=False, verbose_name="Yeni Ürün Mü?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    
    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="Kullanıcı")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Profil Resmi")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon")
    address = models.TextField(blank=True, null=True, verbose_name="Adres")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Şehir")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ülke")
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="Posta Kodu")
    
    class Meta:
        verbose_name = "Kullanıcı Profili"
        verbose_name_plural = "Kullanıcı Profilleri"
    
    def __str__(self):
        return f"{self.user.username} Profili"

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist', verbose_name="Kullanıcı")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Ürün")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")
    
    class Meta:
        verbose_name = "İstek Listesi"
        verbose_name_plural = "İstek Listeleri"
        unique_together = ('user', 'product')
    
    def __str__(self):
        return f"{self.user.username}'in istek listesindeki {self.product.name}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts', verbose_name="Kullanıcı")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    
    class Meta:
        verbose_name = "Sepet"
        verbose_name_plural = "Sepetler"
    
    def __str__(self):
        return f"{self.user.username}'in sepeti"
    
    def get_total_price(self):
        """Sepetteki toplam fiyatı hesaplar"""
        return sum(item.get_cost() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name="Sepet")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Ürün")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Miktar")
    
    class Meta:
        verbose_name = "Sepet Öğesi"
        verbose_name_plural = "Sepet Öğeleri"
        unique_together = ('cart', 'product')
    
    def __str__(self):
        return f"{self.quantity} adet {self.product.name}"
    
    def get_cost(self):
        """Ürünün toplam fiyatını hesaplar"""
        return self.product.price * self.quantity

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Beklemede'),
        ('processing', 'İşleniyor'),
        ('shipped', 'Kargoya Verildi'),
        ('delivered', 'Teslim Edildi'),
        ('canceled', 'İptal Edildi'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="Kullanıcı")
    first_name = models.CharField(max_length=100, verbose_name="Ad")
    last_name = models.CharField(max_length=100, verbose_name="Soyad")
    email = models.EmailField(verbose_name="E-posta")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    address = models.TextField(verbose_name="Adres")
    city = models.CharField(max_length=100, verbose_name="Şehir")
    country = models.CharField(max_length=100, verbose_name="Ülke")
    postal_code = models.CharField(max_length=20, verbose_name="Posta Kodu")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Durum")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    
    class Meta:
        verbose_name = "Sipariş"
        verbose_name_plural = "Siparişler"
        ordering = ('-created_at',)
    
    def __str__(self):
        return f"Sipariş #{self.id}"
    
    def get_total_cost(self):
        """Siparişin toplam fiyatını hesaplar"""
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Sipariş")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Ürün")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Miktar")
    
    class Meta:
        verbose_name = "Sipariş Öğesi"
        verbose_name_plural = "Sipariş Öğeleri"
    
    def __str__(self):
        return f"{self.quantity} adet {self.product.name}"
    
    def get_cost(self):
        """Ürünün toplam fiyatını hesaplar"""
        return self.price * self.quantity

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Blog URL")
    image = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name="Blog Resmi")
    content = models.TextField(verbose_name="İçerik")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="Yazar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    
    class Meta:
        verbose_name = "Blog Yazısı"
        verbose_name_plural = "Blog Yazıları"
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])
