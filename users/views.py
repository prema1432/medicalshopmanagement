from django.shortcuts import render


def index(request):
    context = {}
    context["cart_items_count"] = 23
    return render(request, 'index.html',context)


def about_us(request):
    return render(request, 'aboutus.html')


def cart(request):
    context = {}
    context["cart_items_count"] = 23
    return render(request, 'cart.html', context)


def signin(request):
    return render(request, 'signin.html')


def products(request):
    return render(request, 'products.html')


def customer_signup(request):
    return render(request, 'customer_sign_up.html')


def shop_signup(request):
    return render(request, 'shop_signup.html')
