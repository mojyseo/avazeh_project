from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project 
from django.core.paginator import Paginator
from django.core.mail import send_mail

# Create your views here.

def home(req):
    projects = Project.objects.all() [:3]
    return render(req, 'portfolio/home.html', {'projects': projects})
def home_en(req):
    projects = Project.objects.all() [:3]
    return render(req, 'portfolio/home-en.html', {'projects': projects})


def about(req):
    return render(req, 'portfolio/about.html')
def about_en(req):
    return render(req, 'portfolio/about-en.html')


def products(req):
    projects = Project.objects.all()

    paginator = Paginator(projects, 6)
    
    page = req.GET.get('page')

    projects = paginator.get_page(page)
    
    return render(req, 'portfolio/products.html', {'projects': projects})
def products_en(req):
    projects = Project.objects.all()

    paginator = Paginator(projects, 6)
    
    page = req.GET.get('page')

    projects = paginator.get_page(page)
    return render(req, 'portfolio/products-en.html', {'projects': projects})

def product(req, product_id):
    product = get_object_or_404(Project, pk=product_id)
    return render(req, 'portfolio/product.html' , {'product': product}
)
def product_en(req, product_id):
    product = get_object_or_404(Project, pk=product_id)
    return render(req, 'portfolio/product-en.html' , {'product': product}
)

def contact(req):

    return render(req, 'portfolio/contact.html')
def contact_en(req):
    return render(req, 'portfolio/contact-en.html')

def msg_sent(req):
    fullname = req.GET.get('name')
    email = req.GET.get('email')
    phone = req.GET.get('phone')
    desc = req.GET.get('desc')
    a = req.META
    msg = "name : {} \n email : {} \n phone : {} \n desc : {} \n note from mojy : have a good day with this;)) \n some other data from backend : {}".format(fullname,  email, phone, desc, a)
    send_mail('Avazeh-contact-customer', msg, 'm.madadi.v@gmail.com', ['mojyseo@gmail.com'], fail_silently=True)
    
    return render(req, 'portfolio/msg-sent.html')