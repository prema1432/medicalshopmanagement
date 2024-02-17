from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from users.forms import SignInForm, ShopEditForm, CategoryForm
from users.models import CustomUser, Category


def index(request):
    context = {}
    context["cart_items_count"] = 23
    return render(request, 'index.html', context)


def about_us(request):
    return render(request, 'aboutus.html')


def cart(request):
    context = {}
    context["cart_items_count"] = 23
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
                return redirect('dashboard')
            else:
                return redirect('index')
        else:
            form.add_error(None, 'Invalid username or password')
    context["form"] = form
    return render(request, 'signin.html', context)


def products(request):
    return render(request, 'products.html')


def customer_signup(request):
    return render(request, 'customer_sign_up.html')


def shop_signup(request):
    return render(request, 'shop_signup.html')


def shops(request):
    return render(request, 'shops.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def customers_list(request):
    context = {}
    context['customers'] = CustomUser.objects.filter(role="customer").order_by('-created_at')
    return render(request, 'customers.html', context)


def admin_users_list(request):
    context = {}
    context['customers'] = CustomUser.objects.filter(role="admin").order_by('-created_at')
    return render(request, 'admin_users_list.html', context)


def shops_list(request):
    context = {}
    context['shops'] = CustomUser.objects.filter(role="shop").order_by('-created_at')
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
    return redirect('your_redirect_url_name')


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
    categories = Category.objects.all()
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
    category = get_object_or_404(Category, pk=category_id)
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
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully.')
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})
