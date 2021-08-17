from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json


def index(request):
   # products = Product.objects.all()
  #  print(products)
  #  n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    #params = {'no_of_slide' : nSlides, 'range' : range(1,nSlides), 'product' : products}
   # allProds=[[products,range(1, nSlides), nSlides],
       #     [products, range(1, nSlides), nSlides],
        #    [products,range(1, nSlides), nSlides]]
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(0, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'ecom/index.html', params)


def about(request):
    return render(request, 'ecom/about.html')


def contact(request):
    str = False
    if request.method == "POST":
        name = request.POST.get('name', ' ')
        phone = request.POST.get('phone', ' ')
        email = request.POST.get('email', ' ')
        desc = request.POST.get('desc', ' ')
        print(name, phone, email, desc)
        contact = Contact(name=name, phone=phone, email=email, desc=desc)
        contact.save()
        str = True
    return render(request, 'ecom/contact.html', {'str': str})


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'ecom/tracker.html')


def search(request):
    return render(request, 'ecom/search.html')


def productview(request, id):
    # fetching the product using id
    product = Product.objects.filter(id=id)
    print(product)
    return render(request, 'ecom/productview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Ur Order Have Been Placed")
        update.save()
        str = True
        id = order.order_id
        return render(request, 'ecom/checkout.html', {'str': str, 'id': id})
    return render(request, 'ecom/checkout.html')


def register(request):
    return HttpResponse("Welcome to register")


def login(request):
    return HttpResponse("Welcome to login")


def cart(request):
    return HttpResponse("Welcome to cart")


def category(request):
    return HttpResponse("Welcome to category")


def UserProfile(request):
    return HttpResponse("Welcome to UserProfile")


def wishlist(request):
    return HttpResponse("Welcome to wishlist")



