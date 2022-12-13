from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import *

from django.views.generic.edit import CreateView





class Add(CreateView):
    model = Aqua
    fields = ['name', 'age', 'email', 'phone', 'address']
    template_name = 'add.html'
    success_url = '/aqua/'
    
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        