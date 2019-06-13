from django.shortcuts import render
from . import initiate 

# variables
raffle = ""
firstname = ""
lastname = ""
email = ""
paypal_email = ""
instagram = ""
phone_prefix = ""
phone = ""
address = ""
street1 = ""
street2 = ""
zipcode = ""
county = ""
city = ""
state = ""
country = ""
raffle = ""
api_key = ""
threads = ""
cardname = ""
cardnumber = ""
cc_exp_mo = ""
cc_exp_yr = ""
cvc = ""


# Create your views here.
def index(request):

	return render(request, 'raffle_form/index.html')


# tresbien views
def profile_tres_bien(request):

	global raffle

	raffle = "tresbien"

	return render(request, 'raffle_form/tresbien_raffleform.html')

def preferences_tres_bien(request):

	global firstname,lastname,email,phone,address,city,zipcode,state,country

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

	return render(request, 'raffle_form/tresbien_preferences.html')

def thankyou_tres_bien(request):

	global shoe_size,threads,api_key

	shoe_size = request.POST.get('shoe_size')
	api_key = request.POST.get('api_key')
	threads = request.POST.get('threads')


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
	

	return render(request, 'raffle_form/tresbien_thankyou.html')


# afewstore views
def profile_a_few_store(request):

	global raffle

	raffle = "afewstore"

	return render(request, 'raffle_form/afewstore_raffleform.html')

def preferences_a_few_store(request):

	global firstname,lastname,email,phone,address,city,zipcode,state,country

	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	address = request.POST.get('address')
	zipcode = request.POST.get('zipcode')
	city = request.POST.get('city')
	state = request.POST.get('state')
	country = request.POST.get('country')

	return render(request, 'raffle_form/afewstore_preferences.html')

def thankyou_a_few_store(request):

	global shoe_size,threads,api_key

	shoe_size = request.POST.get('shoe_size')
	api_key = request.POST.get('api_key')
	threads = request.POST.get('threads')


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

	global raffle

	raffle = "jdsports"

	return render(request, 'raffle_form/jdsports_raffleform.html')

def preferences_jd_sports(request):

	global firstname,lastname,email,paypal_email,phone_prefix,phone,street1,street2,city,zipcode,county

	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	paypal_email = request.POST.get('paypal_email')
	street1 = request.POST.get('street1')
	street2 = request.POST.get('street2')
	city = request.POST.get('city')
	zipcode = request.POST.get('zipcode')
	county = request.POST.get('county')

	return render(request, 'raffle_form/jdsports_preferences.html')

def thankyou_jd_sports(request):

	global shoe_size,threads

	shoe_size = request.POST.get('shoe_size')
	threads = request.POST.get('threads')


	initiate.raffle(
		raffle=raffle,
		firstname=firstname,
		lastname=lastname,
		email=email,
		paypal_email=payment_email,
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


def preferences(request):

	global firstname,lastname,email,phone,address,city,zipcode,state,country

	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	phone = request.POST.get('phone')
	address = request.POST.get('address')
	city = request.POST.get('city')
	zipcode = request.POST.get('zipcode')
	state = request.POST.get('state')
	country = request.POST.get('country')


	return render(request, 'raffle_form/preferences.html')

def payment(request):

	global raffle,threads,api_key

	raffle = request.POST.get('raffle')
	api_key = request.POST.get('api_key')
	threads = request.POST.get('threads')

	return render(request, 'raffle_form/payment.html')

def thankyou(request):

	global cardname,cardnumber,cc_exp_mo,cc_exp_yr,cvc

	cardname = request.POST.get('cardname')
	cardnumber = request.POST.get('cardnumber')
	cc_exp_mo = request.POST.get('cc_exp_mo')
	cc_exp_yr = request.POST.get('cc_exp_yr')
	cvc = request.POST.get('cvc')


	initiate.raffle(firstname,lastname,email,phone,address,city,zipcode,state,country,raffle,threads,api_key,cardname,cardnumber,cc_exp_mo,cc_exp_yr,cvc)
	

	return render(request, 'raffle_form/thankyou.html')