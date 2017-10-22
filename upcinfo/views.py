from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import UPCProduct
from django import forms

class SearchForm(forms.Form):
    pid = forms.CharField(label='Search', max_length=100)

def findItemsByProduct(request, pid=None):
    # import pdb ; pdb.set_trace()
    if request.method == 'POST':
        searchform = SearchForm(request.POST or None)
        pid = searchform.data.get('search', 0)
        if not pid:
            pid = 0
        upcrecords = get_object_or_404(UPCProduct, prodid=pid)
        searchform = SearchForm()
        return render(request, 'list.html', {'upcrecords': [upcrecords], 'form': searchform})
    upcrecords = UPCProduct.objects.all()
    searchform = SearchForm(request.POST or None)
    return render(request, 'list.html', {'upcrecords': upcrecords, 'form': searchform})
