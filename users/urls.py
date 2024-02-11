from django.urls import path

from users.views import index, about_us, cart, signin, products, customer_signup, shop_signup, shops, logout_view, \
    dashboard

urlpatterns = [
    path('', index, name='index'),
    path('about_us/', about_us, name='about_us'),
    path('cart/', cart, name='cart'),
    path('signin/', signin, name='signin'),
    path('products/', products, name='products'),
    path('customer_signup/', customer_signup, name='customer_signup'),
    path('shop_signup/', shop_signup, name='shop_signup'),
    path('shops/', shops, name='shops'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
