from django.shortcuts import render
from .models import Element
from django.core import serializers

# Create your views here.

def frontend(request):
    elements = Element.objects.all()
    context = {
        'elements':elements,
        'list':serializers.serialize('json',Element.objects.all())
    }
    return render(request,'index.html',context)