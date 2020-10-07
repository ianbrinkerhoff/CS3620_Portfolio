from django.db import models

# Create your models here.
class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name + ": " + self.hobby_desc + " "

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default="https://www.dreamstime.com/kids-character-various-objects-flat-design-style-isolated-diversity-children-portrait-their-hobbies-vector-cartoon-image178264673")


class Portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name + ": " + self.portfolio_desc + " "

    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=200)
    portfolio_image = models.CharField(max_length=500, default="https://www.edmundsgovtech.com/wp-content/uploads/2020/01/default-picture_0_0.png")

