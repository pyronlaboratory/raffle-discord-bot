from django.urls import path

from . import views

urlpatterns = [
	path('', views.index),
	path('preferences', views.preferences, name='preferences'),
	path('payment', views.payment, name='payment'),
	path('thankyou', views.thankyou, name='thankyou'),
]
