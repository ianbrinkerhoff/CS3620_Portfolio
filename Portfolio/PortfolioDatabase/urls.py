from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('', views.home, name="home"),

    path('hobbies/', views.hobbies, name="hobbies"),
    path('hobbies/<int:h_id>', views.h_detail, name="h_detail"),

    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/<int:p_id>', views.p_detail, name="p_detail"),

    path('contact/', views.contact, name="contact"),
]