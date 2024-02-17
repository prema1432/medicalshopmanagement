from django.urls import path

from users.views import index, about_us, cart, signin, products, customer_signup, shop_signup, shops, logout_view, \
    dashboard, customers_list, admin_users_list, shops_list, delete_user, edit_shop_user, category_list, \
    create_category, edit_category, delete_category

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
    path('customers/', customers_list, name='customers'),
    path('admin_users/', admin_users_list, name='admin_users'),
    path('shops_list/', shops_list, name='shops_list'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('edit_shop_user/<int:user_id>/', edit_shop_user, name='edit_shop_user'),
    path('category_list/', category_list, name='category_list'),
    path('create_category/', create_category, name='create_category'),
    path('edit_category/<int:category_id>/', edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),

]
