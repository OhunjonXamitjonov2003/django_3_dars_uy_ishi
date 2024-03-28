from django.shortcuts import render
from django.http import HttpResponse
from .models import Color,Brand,Car
# Create your views here.




def all_cars(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    context = {
        'cars':cars,
        'brands':brands,
        'colors':colors,
        'title':"Barcha avtomobillar"
    }


    return render(request,'app/index.html',context=context)


def cars_by_brends(request,brand_id):
    cars = Car.objects.filter(brand_id=brand_id)
    brands = Brand.objects.all()
    brand = Brand.objects.get(pk=brand_id)

    context = {
        'cars':cars,
        'brands':brands,
        'title':f"{brand.brand_name} brandiga tegishli avtomobillar",

    }


    return render(request,'app/index.html',context=context)

def cars_by_colors(request,color_id):
    cars = Car.objects.filter(color_id=color_id)
    colors = Color.objects.all()
    color = Color.objects.get(pk=color_id)
    context = {
        'cars':cars,
        'colors':colors,
        'title':f"{color.color_name} rangdagi avtomabillar"
    }
    return render(request,'app/index.html',context=context)
