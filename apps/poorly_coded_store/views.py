from django.shortcuts import render
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    print("POST data")
    print(request.POST)

    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    
    this_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    total_quantity = 0
    total_amount = 0
    for order in Order.objects.all():
        total_quantity += order.quantity_ordered
        total_amount += order.total_price

    context = {
        order: this_order
        total_amount : total_amount,
        total_quantity: total_quantity
    }

    return render(request, "store/checkout.html",context)