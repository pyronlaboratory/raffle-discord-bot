from django.shortcuts import render
from . import initiate 

# variables
raffle = ""
firstname = ""
lastname = ""
email = ""
instagram = ""
phone = ""
address = ""
city = ""
zipcode = ""
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

	global raffle,shoe_size,threads,api_key

	shoe_size = request.POST.get('shoe_size')
	api_key = request.POST.get('api_key')
	threads = request.POST.get('threads')


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

def profile_a_few_store(request):
	return render(request, 'raffle_form/afewstore_raffleform.html')

def preferences_a_few_store(request):
	return render(request, 'raffle_form/afewstore_preferences.html')

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