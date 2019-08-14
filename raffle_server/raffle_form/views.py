import json

from django.shortcuts import render
from . import initiate 
from .models import Raffle


# Create your views here.
def index(request):
        features=[]
        with open(r"C:\Users\AYUSH\Desktop\Ronnie\python\discord-raffle-bot\raffle_server\raffle_form\scripts\tools\config\urls.json") as json_file: # update address on production server
                url_dictionary = json.load(json_file)
                for raffle in url_dictionary:
                	features.append(url_dictionary[raffle]['shoe'])



        return render(request, 'raffle_form/index.html', {"features":features})





# tresbien views
def profile_tres_bien(request):
	

	return render(request, 'raffle_form/tresbien_raffleform.html')


def thankyou_tres_bien(request):

	raffle = "tresbien"
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	phone = request.POST.get('phone')
	address = request.POST.get('address')
	city = request.POST.get('city')
	zipcode = request.POST.get('zipcode')
	state = request.POST.get('state')
	country = request.POST.get('country')
	shoe_size = request.POST.get('shoe_size')
	api_key = request.POST.get('api_key')
	threads = request.POST.get('threads')

	raffle_entry = Raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		phone=phone,
		address=address,
		city=city,
		zipcode=zipcode,
		state=state,
		country=country,
		shoe_size=shoe_size,
		api_key=api_key,
		threads=threads)
	
	raffle_entry.save()

	initiate.raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		phone=phone,
		address=address,
		city=city,
		zipcode=zipcode,
		state=state,
		country=country,
		shoe_size=shoe_size,
		api_key=api_key,
		threads=threads)

	return render(request, 'raffle_form/tresbien_thankyou.html')





# afewstore views
def profile_a_few_store(request):

	return render(request, 'raffle_form/afewstore_raffleform.html')


def thankyou_a_few_store(request):
	
	raffle = "afewstore"
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	address = request.POST.get('address')
	zipcode = request.POST.get('zipcode')
	city = request.POST.get('city')
	state = request.POST.get('state')
	country = request.POST.get('country')
	shoe_size = request.POST.get('shoe_size')
	api_key = request.POST.get('api_key')
	threads = request.POST.get('threads')

	raffle_entry = Raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		address=address,
		city=city,
		zipcode=zipcode,
		state=state,
		country=country,
		shoe_size=shoe_size,
		api_key=api_key,
		threads=threads)

	raffle_entry.save()
	
	initiate.raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		address=address,
		city=city,
		zipcode=zipcode,
		state=state,
		country=country,
		shoe_size=shoe_size,
		api_key=api_key,
		threads=threads)
	
	return render(request, 'raffle_form/afewstore_thankyou.html')





# jdsports views
def profile_jd_sports(request):

	return render(request, 'raffle_form/jdsports_raffleform.html')


def thankyou_jd_sports(request):
	
	raffle = "jdsports"
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	paypal_email = request.POST.get('paypal_email')
	phone_prefix = request.POST.get('phone_prefix')
	phone = request.POST.get('phone')
	street1 = request.POST.get('street1')
	street2 = request.POST.get('street2')
	city = request.POST.get('city')
	zipcode = request.POST.get('zipcode')
	county = request.POST.get('county')
	shoe_size = request.POST.get('shoe_size')
	threads = request.POST.get('threads')

	raffle_entry = Raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		paypal_email=paypal_email,
		phone_prefix=phone_prefix,
		phone=phone,
		street1=street1,
		street2=street2,
		city=city,
		zipcode=zipcode,
		county=county,
		shoe_size=shoe_size,
		threads=threads)

	raffle_entry.save()

	initiate.raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		paypal_email=paypal_email,
		phone_prefix=phone_prefix,
		phone=phone,
		street1=street1,
		street2=street2,
		city=city,
		zipcode=zipcode,
		county=county,
		shoe_size=shoe_size,
		threads=threads)
	
	return render(request, 'raffle_form/jdsports_thankyou.html')





# shizoparis views	
def profile_shinzo_paris(request):
	
	return render(request, 'raffle_form/shinzoparis_raffleform.html')


def thankyou_shinzo_paris(request):
	
	raffle = "shinzoparis"
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	instagram = request.POST.get('instagram')
	phone = request.POST.get('phone')
	address = request.POST.get('address')
	city = request.POST.get('city')
	zipcode = request.POST.get('zipcode')
	state = request.POST.get('state')
	country = request.POST.get('country')
	shoe_size = request.POST.get('shoe_size')
	api_key = request.POST.get('api_key')
	threads = request.POST.get('threads')

	raffle_entry = Raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		instagram=instagram,
		phone=phone,
		address=address,
		city=city,
		zipcode=zipcode,
		state=state,
		country=country,
		shoe_size=shoe_size,
		api_key=api_key,
		threads=threads)
	
	raffle_entry.save()

	initiate.raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		instagram=instagram,
		phone=phone,
		address=address,
		city=city,
		zipcode=zipcode,
		state=state,
		country=country,
		shoe_size=shoe_size,
		api_key=api_key,
		threads=threads)

	return render(request, 'raffle_form/shinzoparis_thankyou.html')





# chmielna20 views	
def profile_chmielna20(request):

	return render(request, 'raffle_form/chmielna20_raffleform.html')


def thankyou_chmielna20(request):
	
	raffle = "chmielna20"
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	phone_prefix = request.POST.get('phone_prefix')
	phone = request.POST.get('phone')
	dob = request.POST.get('dob') 
	city = request.POST.get('city')
	country = request.POST.get('country')
	shoe_size = request.POST.get('shoe_size')
	api_key = request.POST.get('api_key')
	threads = request.POST.get('threads')
	print("collecting chmielna20 details")
	raffle_entry = Raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		phone_prefix=phone_prefix,
		phone=phone,
		dob=dob,
		city=city,
		country=country,
		shoe_size=shoe_size,
		api_key=api_key,
		threads=threads)
	
	raffle_entry.save()
	print("saving chmielna20 object")
	initiate.raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		phone_prefix=phone_prefix,
		phone=phone,
		dob=dob,
		city=city,
		country=country,
		shoe_size=shoe_size,
		api_key=api_key,
		threads=threads)
	print("call sent to initiate")
	return render(request, 'raffle_form/chmielna20_thankyou.html')
