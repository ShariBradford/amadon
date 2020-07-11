from django.shortcuts import render, redirect
from .models import Order, Product

context = {}

def index(request):
    context["all_products"] = Product.objects.all()
    return render(request, "store/index.html", context)

def checkout(request):
    print("POST data")
    print(request.POST)

    quantity_from_form = int(request.POST["quantity"])
    #price_from_form = float(request.POST["price"])
    lookup_price = Product.objects.get(id=request.POST["product_id"]).price
    total_charge = quantity_from_form * lookup_price
    print(f"Charging credit card... {total_charge}")
    
    this_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect(f"/confirm/{this_order.id}")

def confirm_order(request,order_id):
    total_quantity = 0
    total_amount = 0
    for order in Order.objects.all():
        total_quantity += order.quantity_ordered
        total_amount += order.total_price

    context["order"] = Order.objects.get(id=order_id)
    context["total_amount"] = total_amount
    context["total_quantity"] =  total_quantity
    return render(request, "store/checkout.html", context)
