from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('couldson_shelter/', views.couldson_shelter, name='couldson_shelter'),
    path('brixton_hub/', views.brixton_hub, name='brixton_hub'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('rent_a_shelter_resident/', views.rent_a_shelter_resident, name='rent_a_shelter_resident'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('book_an_encounter/', views.book_an_encounter, name='book_an_encounter'),
    path('book_an_encounter_paddy_pony/', views.book_an_encounter_paddy_pony, name='book_an_encounter_paddy_pony'),
    path('all_animal_residents/', views.all_animal_residents, name='all_animal_residents'),
    path('animal_profile/<slug:slug>/<id>/', views.animal_profile, name='animal_profile'),
    path('animal_profile/paddy_pony/', views.paddy_pony, name='paddy_pony'),
    path('admin-interface/logo/green-logo.png/', views.serve_logo, name='serve_logo'),
    path('admin-interface/favicon/green-logo.png/', views.serve_logo, name='serve_logo'),
]