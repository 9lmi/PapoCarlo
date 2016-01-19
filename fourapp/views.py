from django.shortcuts import render
from fourapp.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from fourapp.form import ContactForm
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from datetime import *
import random
import string

# Create your views here.



def home(request):
    category = Category.objects.all()
    context = {
        'sitename': 'Интернет-магазин',
        'categories': category,
    }
    return HttpResponse(render_to_string('home.html', context))

def order(request):
    if request.method == 'GET':
        context = (
            csrf(request)
        )
        return render(request, 'korzina.html', context)
    elif request.method == 'POST':
        try:
            zakaz = Zakaz(name=request.POST['name'], phone=request.POST['phone'], summa=request.POST['hhh2'], zakaz1=request.POST['hh3'],)
            zakaz.save()
            return HttpResponseRedirect("/")
        except:
            return HttpResponse("Что-то пошло не так. Проверьте введённые данные.")
    else:
        return HttpResponse("¯\_(ツ)_/¯")

def item(request, alias):
    try:
        tovar = Item.objects.get(alias=alias)
    except:
        raise Http404('Not found')
    context = {
        'tovar': tovar,
    }
    return HttpResponse(render_to_string('item.html', context))

def get_category(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        tovars = Item.objects.filter(category=category)
    except:
        raise Http404('Not found')
    context = {
        'tovars': tovars,
        'category': category,
    }
    return HttpResponse(render_to_string('index.html', context))