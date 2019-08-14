from django.db import models
from . import initiate 

# Create your models here.
class Raffle(models.Model):
	
	raffle = models.CharField(max_length=30)
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	paypal_email = models.EmailField(max_length=30)
	instagram = models.CharField(max_length=30)
	phone_prefix = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	dob = models.CharField(max_length=15)
	address = models.CharField(max_length=60)
	street1 = models.CharField(max_length=30)
	street2 = models.CharField(max_length=30)
	zipcode = models.CharField(max_length=30)
	county = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	shoe_size = models.CharField(max_length=30)
	api_key = models.CharField(max_length=50)
	threads = models.CharField(max_length=30)
	cardname = models.CharField(max_length=30)
	cardnumber = models.CharField(max_length=30)
	cc_exp_mo = models.CharField(max_length=30)
	cc_exp_yr = models.CharField(max_length=30)
	cvc = models.CharField(max_length=30)

	def __str__(self):
		return self.raffle+'_entry'
