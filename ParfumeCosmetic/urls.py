from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home_cosmetic, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product/', views.product, name='product'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('product-default/', views.product_default, name='product_default'),
    path('blog/', views.blog_main, name='blog'),
    path('blog/post/<slug:blog_slug>/', views.blog_post_detail, name='blog_post_detail'),
    path('blog-post/', views.blog_post, name='blog_post'),
    path('blog-post-new/', views.blog_post_new, name='blog_post_new'),
    path('contact/', views.contact, name='contact'),
    path('shop-default/', views.shop_default, name='shop_default'),
    path('shop-grid/', views.shop_grid, name='shop_grid'),
    
    # Kullanıcı işlemleri
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('reset-password/', views.reset_password, name='reset_password'),
    
    # Sepet işlemleri
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-complete/<int:order_id>/', views.order_complete, name='order_complete'),
    path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),
    
    # İstek listesi işlemleri
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    # Sayfalar
    path('about/', views.about, name='about'),
    path('typography/', views.page_typography, name='typography'),
] 