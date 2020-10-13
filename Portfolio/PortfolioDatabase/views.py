from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobby
from .models import Portfolio
from .forms import PortfolioForm
from .forms import ContactForm
from django.template import loader
from django .contrib.auth.forms import UserCreationForm
from django .contrib import messages


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
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        contact_name = form.cleaned_data.get('contact_name')
        messages.success(request, f'Thanks {contact_name}! Your contact information was received.')
        return redirect('PortfolioDatabase:contact')

    return render(request, 'portfolio/contact.html', {'form': form})


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


def add_portfolio(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'portfolio/portfolio-form.html', {'form': form})


def update_portfolio(request, id):
    portfolio = Portfolio.objects.get(id=id)
    form = PortfolioForm(request.POST or None, instance=portfolio)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'portfolio/portfolio-form.html', {'form': form, 'portfolio': portfolio})


def delete_portfolio(request, id):
    portfolio = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        portfolio.delete()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'portfolio/portfolio-delete.html', {'portfolio': portfolio})