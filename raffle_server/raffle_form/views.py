from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'raffle_form/raffleform.html')

def preferences(request):
	print(request.POST.get('firstname'))
	return render(request, 'raffle_form/preferences.html')

def payment(request):
	print(request.POST.get('2Captcha'))
	return render(request, 'raffle_form/payment.html')

def thankyou(request):
	if request.method == 'POST':
		print(request.POST.get('firstname'))
		return render(request, 'raffle_form/thankyou.html')