from django.shortcuts import render
from django.views.generic import ListView 
from .models import Profile
from profiles.forms import Profileforms
# Create your views here.

def HomeView(request):
    forms = Profileforms()
    
    if request.POST:
        
        if forms.is_valid():
            forms.save()
    
    return render(request, 'index.html', {'forms': forms})

            
         
class staffs(ListView):
    model = Profile
    template_name= 'staffs.html'
    fields = '__all__'
    