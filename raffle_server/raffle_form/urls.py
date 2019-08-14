from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),

	path('profile_tres_bien', views.profile_tres_bien, name='profile_tres_bien'),
	path('thankyou_tres_bien', views.thankyou_tres_bien, name='thankyou_tres_bien'),
	
	path('profile_a_few_store', views.profile_a_few_store, name='profile_a_few_store'),
	path('thankyou_a_few_store', views.thankyou_a_few_store, name='thankyou_a_few_store'),
	
	path('profile_jd_sports', views.profile_jd_sports, name='profile_jd_sports'),
	path('thankyou_jd_sports', views.thankyou_jd_sports, name='thankyou_jd_sports'),

	path('profile_shinzo_paris', views.profile_shinzo_paris, name='profile_shinzo_paris'),
	path('thankyou_shinzo_paris', views.thankyou_shinzo_paris, name='thankyou_shinzo_paris'),

	path('profile_chmielna20', views.profile_chmielna20, name='profile_chmielna20'),
	path('thankyou_chmielna20', views.thankyou_chmielna20, name='thankyou_chmielna20'),	

]
