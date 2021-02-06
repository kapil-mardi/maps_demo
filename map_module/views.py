from django.shortcuts import render
from .models import State, District, Category, Taluka

# Create your views here.

def home(request):
    context = {
        "states" : State.objects.all(),
        "categories" : Category.objects.all()
    }
    return render(request,'maps/home.html',context)


def load_districts(request):
    state_id = request.GET.get('state')
    category_id = request.GET.get('category')
    districts = District.objects.filter(state_id = state_id, category_id = category_id).order_by('name')
    return render(request, 'maps/list.html', {'datas': districts})

def load_talukas(request):
    district_id = request.GET.get('district')
    talukas = Taluka.objects.filter(district_id = district_id).order_by('name')
    return render(request, 'maps/list.html', {'datas': talukas})
