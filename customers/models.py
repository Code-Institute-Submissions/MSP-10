from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


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

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    address1 = models.CharField(max_length=100, null=True, blank=True)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    address3 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, choices=COUNTRIES)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    subscription = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
