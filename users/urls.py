from django.urls import path

from users.views import index, about_us, cart, signin, products, customer_signup, shop_signup, shops, logout_view, \
    dashboard, customers_list, admin_users_list, shops_list, delete_user, edit_shop_user, category_list, \
    create_category, edit_category, delete_category, product_list, product_detail, product_create, product_update, \
    product_delete, add_to_cart, update_cart_item, remove_cart_item, clear_cart

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
    path('products_list/', product_list, name='products_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('product/create/', product_create, name='product_create'),
    path('product/<int:product_id>/update/', product_update, name='product_update'),
    path('product/<int:product_id>/delete/', product_delete, name='product_delete'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/update/<int:cart_item_id>/', update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:cart_item_id>/', remove_cart_item, name='remove_cart_item'),
    path('cart/clear/', clear_cart, name='clear_cart'),

]
