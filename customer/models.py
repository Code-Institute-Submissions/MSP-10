from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    COUNTRIES = (
        ('Austria', 'Austria'),
        ('Belgium', 'Belgium'),
        ('Bulgaria', 'Bulgaria'),
        ('Croatia', 'Croatia'),
        ('Cyprus', 'Cyprus'),
        ('Czechia', 'Czechia'),
        ('Denmark', 'Denmark'),
        ('Estonia', 'Estonia'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Germany', 'Germany'),
        ('Greece', 'Greece'),
        ('Hungary', 'Hungary'),
        ('Ireland', 'Ireland'),
        ('Italy', 'Italy'),
        ('Latvia', 'Latvia'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Malta', 'Malta'),
        ('Netherlands', 'Netherlands'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Romania', 'Romania'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Spain', 'Spain'),
        ('Sweden', 'Sweden'),
    )
    
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    address1 = models.CharField(max_length=100, null=True, blank=True)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    address3 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, choices=COUNTRIES)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.username