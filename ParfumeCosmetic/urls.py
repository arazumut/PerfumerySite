from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home_cosmetic, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product/', views.product, name='product'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('product-default/', views.product_default, name='product_default'),
    path('blog/', views.blog_main, name='blog'),
    path('blog-post/', views.blog_post, name='blog_post'),
    path('blog-post-new/', views.blog_post_new, name='blog_post_new'),
    path('contact/', views.contact, name='contact'),
    path('shop-default/', views.shop_default, name='shop_default'),
    path('shop-grid/', views.shop_grid, name='shop_grid'),
    path('login/', views.login_view, name='login'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('about/', views.about, name='about'),
    path('typography/', views.page_typography, name='typography'),
] 