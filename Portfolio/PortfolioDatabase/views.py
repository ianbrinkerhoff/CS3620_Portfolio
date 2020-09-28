from django.shortcuts import render
from django.http import HttpResponse
from . models import Hobby
from . models import Portfolio


# Create your views here.
def home(request):
    return HttpResponse('<h1>Portfolio Home</h1>'
                        '<p>Hello! My name is Ian Brinkerhoff, '
                        'I am a senior in the CS program at Weber State. '
                        'I work full time as a Unit Training Manager in an Air Force '
                        'Unit on base. I am married to a wonderful nurse named '
                        'Baylee, and I have been living in Mississippi on an Air Force '
                        'base for the last 2 months and I officially come home to Utah '
                        'this week!</p>')


def hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)


def contact(request):
    return HttpResponse('<h1>Contact Information:</h1>'
                        '<p>email: ianbrinkerhoff@mail.weber.edu<p>')

