from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django import forms
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description']
def item_list(request):
    q = request.GET.get('q','')
    if q:
        items = Item.objects.filter(name__icontains=q)
    else:
        items = Item.objects.all()
    return render(request, 'menu/item_list.html', {'items': items, 'q': q})
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu:item_list')
    else:
        form = ItemForm()
    return render(request, 'menu/item_form.html', {'form': form})
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu:item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'menu/item_form.html', {'form': form})
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('menu:item_list')
    return render(request, 'menu/item_confirm_delete.html', {'item': item})
