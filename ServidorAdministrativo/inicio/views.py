from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    usuarios=User.objects.all()
    data={'usuarios': usuarios}
    return render(request, 'inicio/home.html', data)