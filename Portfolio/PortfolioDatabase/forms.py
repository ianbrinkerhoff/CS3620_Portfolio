from django import forms
from .models import Portfolio
from .models import Contact


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['portfolio_name', 'portfolio_desc', 'portfolio_image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_message']

