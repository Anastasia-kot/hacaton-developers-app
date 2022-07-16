from calendar import c
from distutils.command.clean import clean
from sqlite3 import Cursor
from django.db import models

# Create your models here.


class RealEstateOwner(models.Model):

    name = models.CharField(max_length=255)


class RealEstate(models.Model):

    owner = models.ForeignKey(RealEstateOwner, on_delete=models.CASCADE)
    area_type = models.IntegerField()
    region = models.CharField(max_length=255)
    realestate_type = models.IntegerField()
    period = models.IntegerField()
    relation = models.IntegerField()
    dt = models.DateTimeField(auto_now_add=True)


class FreelanceAgent(models.Model):
    
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class AgentInvestor(models.Model):

    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Agency(models.Model):

    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class AgencyWorker(models.Model):

    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Tag(models.Model):

    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class PriceStory(models.Model):

    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    price = models.CharField(max_length=255)
    dt = models.DateField(auto_now_add=True)


class Gold(models.model):

    rate = models.CharField(max_length=255)
    dt = models.DateField(auto_now_add=True)


class Dollar(models.model):
    
    rate = models.CharField(max_length=255)
    dt = models.DateField(auto_now_add=True)


class Euro(models.model):

    rate = models.CharField(max_length=255)
    dt = models.DateField(auto_now_add=True)


class Btc(models.Model):

    rate = models.CharField(max_length=255)
    dt = models.DateField(auto_now_add=True)
