from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum, F
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from users.forms import SignInForm, ShopEditForm, CategoryForm, MedicalProductForm, CustomerForm, ShopUserForm
from users.models import CustomUser, MedicalProductCategory, MedicalProduct, Cart


# categories = MedicalProductCategory.objects.annotate(num_products=Count('medicalproduct')).order_by('-num_products')

def index(request):
    context = {}
    products = MedicalProduct.objects.all().order_by('-created_at')[:10]
    context = {'products': products}
    context["cart_items_count"] = 0
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count
    return render(request, 'index.html', context)


def about_us(request):
    context = {}
    context["cart_items_count"] = 0
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count
    return render(request, 'aboutus.html', context)


@login_required
def cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    cart_items_count = cart_items.count()
    context = {
        'cart_items_count': cart_items_count,
        'cart_items': cart_items
    }
    return render(request, 'cart.html', context)


def signin(request):
    context = {}
    form = SignInForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role in ["admin"]:
                messages.success(request, "Login successful.")
                return redirect('dashboard')
            else:
                messages.success(request, "Login successful.")
                return redirect('index')
        else:
            messages.warning(request, "Invalid username or password")
            form.add_error(None, 'Invalid username or password')
    context["form"] = form
    return render(request, 'signin.html', context)


def products(request):
    context = {}
    context["cart_items_count"] = 0
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count
    context["categories"] = MedicalProductCategory.objects.annotate(num_products=Count('medicalproduct')).order_by(
        '-num_products')
    return render(request, 'products.html', context)


def customer_signup(request):
    context = {}
    context["cart_items_count"] = 0
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            role = "CUSTOMER"
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            my_username = f"{role[:2].upper()}000{user.id}"
            user.username = my_username
            user.save()
            messages.success(request, f'{user.username} - User created successfully.')
            return redirect('signin')
    else:
        form = CustomerForm()

    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count

    context['form'] = form
    return render(request, 'customer_sign_up.html', context)


def shop_signup(request):
    context = {}
    context["cart_items_count"] = 0
    if request.method == 'POST':
        form = ShopUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            role = "SHOP"
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            my_username = f"{role[:2].upper()}000{user.id}"
            user.username = my_username
            user.save()
            messages.success(request, f'{user.username} - User created successfully.')
            return redirect('signin')
    else:
        form = ShopUserForm()
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count

    context['form'] = form
    return render(request, 'shop_signup.html', context)


def shops(request):
    context = {}
    context['shops'] = CustomUser.objects.filter(role="shop").order_by('-created_at')
    context["cart_items_count"] = 0
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count
    return render(request, 'shops.html', context)


@login_required
def dashboard(request):
    context = {}
    context["cart_items_count"] = 0
    admin_count = CustomUser.objects.filter(role='admin').count()
    shop_count = CustomUser.objects.filter(role='shop').count()
    customer_count = CustomUser.objects.filter(role='customer').count()

    # Count total number of products and categories
    total_products_count = MedicalProduct.objects.count()
    total_categories_count = MedicalProductCategory.objects.count()

    # Set counts in context
    context['admin_count'] = admin_count
    context['shop_count'] = shop_count
    context['customer_count'] = customer_count
    context['total_products_count'] = total_products_count
    context['total_categories_count'] = total_categories_count
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count
    return render(request, 'dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def customers_list(request):
    context = {}
    context['customers'] = CustomUser.objects.filter(role="customer").order_by('-created_at')
    context["cart_items_count"] = 0
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count
    return render(request, 'customers.html', context)


def admin_users_list(request):
    context = {}
    context['customers'] = CustomUser.objects.filter(role="admin").order_by('-created_at')
    context["cart_items_count"] = 0
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count
    return render(request, 'admin_users_list.html', context)


def shops_list(request):
    context = {}
    context['shops'] = CustomUser.objects.filter(role="shop").order_by('-created_at')
    context["cart_items_count"] = 0
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
        context['cart_items_count'] = cart_items_count
    return render(request, 'shops_list.html', context)


def delete_shop(request, shop_id):
    if request.method == 'POST':
        shop = get_object_or_404(CustomUser, id=shop_id, role="shop")
        shop.delete()
        return redirect('shops_list')
    else:
        return HttpResponseBadRequest("Invalid request method")


def delete_user(request, user_id):
    try:
        obj = CustomUser.objects.get(id=user_id)
        role_based = obj.role
        obj.delete()
        messages.success(request, f'{role_based} deleted successfully.')
    except CustomUser.DoesNotExist:
        messages.error(request, f'Id does not exist.')
    if role_based == 'admin':
        return redirect('admin_users_list')
    elif role_based == 'shop':
        return redirect('shops_list')
    elif role_based == 'customer':
        return redirect('customers_list')


def edit_shop_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'POST':
        form = ShopEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User details updated successfully.')
            role_based = user.role
            if role_based == 'admin':
                return redirect('admin_users_list')
            elif role_based == 'shop':
                return redirect('shops_list')
            elif role_based == 'customer':
                return redirect('customers_list')
        else:
            messages.error(request, 'Error updating shop details. Please check the form.')
    else:
        form = ShopEditForm(instance=user)

    return render(request, 'edit_shop_user.html', {'form': form, 'user': user})


def category_list(request):
    categories = MedicalProductCategory.objects.all().order_by('-created_at')
    return render(request, 'category_list.html', {'categories': categories})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully.')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})


def edit_category(request, category_id):
    category = get_object_or_404(MedicalProductCategory, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})


def delete_category(request, category_id):
    try:
        category = get_object_or_404(MedicalProductCategory, pk=category_id)
        category.delete()
        messages.success(request, 'Category deleted successfully.')
        return redirect('category_list')
    except Exception as e:
        messages.error(request, f'Id does not exist.')
        return redirect('category_list')


def product_list(request):
    context = {}
    context['products'] = MedicalProduct.objects.all().order_by('-created_at')
    return render(request, 'product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(MedicalProduct, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = MedicalProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = MedicalProductForm()
    return render(request, 'product_form.html', {'form': form})


def product_update(request, product_id):
    product = get_object_or_404(MedicalProduct, pk=product_id)
    if request.method == 'POST':
        form = MedicalProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = MedicalProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})


def product_delete(request, product_id):
    try:
        product = get_object_or_404(MedicalProduct, pk=product_id)
        product.delete()
        messages.success(request, 'Product deleted successfully.')
    except MedicalProduct.DoesNotExist:
        messages.error(request, 'Product does not exist.')
    return redirect('product_list')


@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = MedicalProduct.objects.get(pk=product_id)
        quantity = request.POST.get('quantity')
        user = request.user
        # Create or update cart entry
        cart, created = Cart.objects.get_or_create(user=user, product=product)
        cart.quantity = quantity
        cart.save()
        messages.success(request, 'Product added to cart successfully.')
    return redirect('index')


@login_required
def cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    cart_items_count = cart_items.count()
    # for item in cart_items:
    #     item.total_price = item.product.price * item.quantity
    # total_price = cart_items.aggregate(total_price=Sum(F('total_price')))['total_price']
    total_price = cart_items.aggregate(total_price=Sum(F('product__price') * F('quantity')))['total_price']
    context = {
        'cart_items_count': cart_items_count,
        'cart_items': cart_items,
        'total_price': total_price

    }
    return render(request, 'cart.html', context)


@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')


@login_required
def remove_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


@login_required
def clear_cart(request):
    user = request.user
    Cart.objects.filter(user=user).delete()
    return redirect('cart')
