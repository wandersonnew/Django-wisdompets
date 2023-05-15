from django.shortcuts import render
from django.http import HttpResponse, Http404

# Import your models here
from .models import Pet

# Create your views here.
def home(request):
    # return HttpResponse('<p>Home View</p>')
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets
    })
        

def pet_detail(request, pet_id):
    # return HttpResponse(f'<p>pet_deatil view with id {pet_id}</p>')
    try:
        pet = Pet.objects.get(id = pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found!')
    return render(request, 'pet_detail.html', {
        'pet': pet
    })
    