from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from menu.models import Item
from customers.models import Customer
from django import forms
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer','phone']
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item','quantity']
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('orders:add_items', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})
def add_items(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            oi = form.save(commit=False)
            oi.order = order
            oi.save()
            return redirect('orders:order_detail', pk=order.pk)
    else:
        form = OrderItemForm()
    items = Item.objects.all()
    return render(request, 'orders/add_items.html', {'order': order, 'form': form, 'items': items})
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})
