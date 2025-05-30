from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('products', views.ProductViewSet)
router.register('users', views.UserViewSet)
router.register('profiles', views.UserProfileViewSet)
router.register('wishlist', views.WishListViewSet, basename='wishlist')
router.register('cart', views.CartViewSet, basename='cart')
router.register('orders', views.OrderViewSet, basename='orders')
router.register('blogs', views.BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]