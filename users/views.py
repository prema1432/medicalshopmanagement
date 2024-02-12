from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import SignInForm
from users.models import CustomUser


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
    context['customers'] = CustomUser.objects.all()
    return render(request, 'customers.html', context)

def admin_users_list(request):
    context = {}
    context['customers'] = CustomUser.objects.all()
    return render(request, 'admin_users_list.html', context)
