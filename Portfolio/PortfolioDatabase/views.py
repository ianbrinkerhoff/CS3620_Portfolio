from django.shortcuts import render
from django.http import HttpResponse
from . models import Hobby
from . models import Portfolio
from django.template import loader


# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')


def hobbies(request):
    hobby_list = Hobby.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'portfolio/hobby.html', context)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, 'portfolio/portfolio.html', context)


def contact(request):
    return render(request, 'portfolio/contact.html')


def p_detail(request, p_id):
    portfolio = Portfolio.objects.get(pk=p_id)
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'portfolio/p_detail.html', context)


def h_detail(request, h_id):
    hobby = Hobby.objects.get(pk=h_id)
    context = {
        'hobby': hobby,
    }
    return render(request, 'portfolio/h_detail.html', context)

