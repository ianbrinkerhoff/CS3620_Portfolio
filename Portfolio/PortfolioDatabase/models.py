from django.db import models

# Create your models here.
class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name + ": " + self.hobby_desc + " "

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=200)


class Portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name + ": " + self.portfolio_desc + " "

    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=200)

