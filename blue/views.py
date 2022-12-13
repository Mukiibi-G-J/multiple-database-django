from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from aqua.models import *

# Create your views here.




def viewsdata(request):
    data = Blue.objects.using('blue_db').all()
    
    
class Add(CreateView):
    model= Blue
    fields = ['name', 'age', 'email', 'phone', 'address']
    template_name = 'add.html'
    success_url = '/blue/'