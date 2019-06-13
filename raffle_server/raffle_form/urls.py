from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('profile_tres_bien', views.profile_tres_bien, name='profile_tres_bien'),
	path('preferences_tres_bien', views.preferences_tres_bien, name='preferences_tres_bien'),
	path('thankyou_tres_bien', views.thankyou_tres_bien, name='thankyou_tres_bien'),
	path('profile_a_few_store', views.profile_a_few_store, name='profile_a_few_store'),
	path('preferences_a_few_store', views.preferences_a_few_store, name='preferences_a_few_store'),
	path('preferences', views.preferences, name='preferences'),
	path('payment', views.payment, name='payment'),
	path('thankyou', views.thankyou, name='thankyou'),
]
