from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from .models import AnimalResident, DragonShelterProfile, BookAnEncounterRequest, DragonShelterEvent, PaddyPony
import os
from django.conf import settings

# Create your models here.
def index(request):
    animal_residents = AnimalResident.objects.all().order_by('-id')[:3][::-1]
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'index.html', {'animal_residents': animal_residents, 'dragon_shelter':dragon_shelter})

def all_animal_residents(request):
    animal_residents = AnimalResident.objects.all()
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'all_animal_residents.html', {'animal_residents': animal_residents, 'dragon_shelter':dragon_shelter})

def book_an_encounter(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        event_description = request.POST.get('event_description')
        preferred_date_of_event = request.POST.get('preferred_date_of_event')

        event_exists = DragonShelterEvent.objects.filter(event_date=preferred_date_of_event).exists()

        if event_exists:
            error = {
                "error": True,
                "message": "Sorry, the date you selected is already booked. Please choose another date for your event. Thanks."
            }
            return JsonResponse(error, status=400)
        else:
            book_an_encounter_request = BookAnEncounterRequest(
                name=name,
                email=email,
                phone_number=phone_number,
                event_description=event_description,
                preferred_date_of_event=preferred_date_of_event,
            )
        
            book_an_encounter_request.save()

            email_subject = 'Reptile Encounter/Party Request Received'
            email_body = render_to_string('email_template.html', {
                'name': name,
                'email': email,
                'phone_number': phone_number,
                'event_description': event_description,
                'preferred_date_of_event': preferred_date_of_event,
                'dragon_shelter_phone_number': dragon_shelter.phone_number,
                'dragon_shelter_whatsapp_number': dragon_shelter.whatsapp_number,
            })

            # Send the email
            msg = EmailMessage(email_subject, email_body, to=[email, 'anna@thedragonshelter.com', 'rachelbooksthedragonshelter@gmail.com'])
            msg.content_subtype = 'html'
            msg.send()

            return render(request, 'book_an_encounter.html', {'dragon_shelter':dragon_shelter})
    else:
        return render(request, 'book_an_encounter.html', {'dragon_shelter':dragon_shelter})
    

def book_an_encounter_paddy_pony(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        event_description = request.POST.get('event_description')
        preferred_date_of_event = request.POST.get('preferred_date_of_event')

        event_exists = DragonShelterEvent.objects.filter(event_date=preferred_date_of_event).exists()

        if event_exists:
            error = {
                "error": True,
                "message": "Sorry, the date you selected is already booked. Please choose another date for your event. Thanks."
            }
            return JsonResponse(error, status=400)
        else:
            book_an_encounter_request = BookAnEncounterRequest(
                name=name,
                email=email,
                phone_number=phone_number,
                event_description=event_description,
                preferred_date_of_event=preferred_date_of_event,
            )
        
            book_an_encounter_request.save()

            email_subject = 'Paddy Pony Encounter/Party Request Received'
            email_body = render_to_string('email_template.html', {
                'name': name,
                'email': email,
                'phone_number': phone_number,
                'event_description': event_description,
                'preferred_date_of_event': preferred_date_of_event,
                'dragon_shelter_phone_number': dragon_shelter.phone_number,
                'dragon_shelter_whatsapp_number': dragon_shelter.whatsapp_number,
            })

            # Send the email
            msg = EmailMessage(email_subject, email_body, to=[email, 'anna@thedragonshelter.com'])
            msg.content_subtype = 'html'
            msg.send()

            return render(request, 'book_an_encounter_paddy_pony.html', {'dragon_shelter':dragon_shelter})
    else:
        return render(request, 'book_an_encounter_paddy_pony.html', {'dragon_shelter':dragon_shelter})


def contact(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'contact.html', {'dragon_shelter':dragon_shelter})

def rent_a_shelter_resident(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'rent_a_shelter_resident.html', {'dragon_shelter':dragon_shelter})

def couldson_shelter(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'couldson_shelter.html', {'dragon_shelter':dragon_shelter})

def brixton_hub(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'brixton_hub.html', {'dragon_shelter':dragon_shelter})

def team(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'team.html', {'dragon_shelter':dragon_shelter})

def testimonial(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'testimonial.html', {'dragon_shelter':dragon_shelter})

def about(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'about.html', {'dragon_shelter':dragon_shelter})

def services(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    return render(request, 'services.html', {'dragon_shelter':dragon_shelter})

def animal_profile(request, slug, id):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    animal = get_object_or_404(AnimalResident, pk=id)
    return render(request, 'animal_profile.html', {'animal': animal, 'dragon_shelter':dragon_shelter})


def paddy_pony(request):
    dragon_shelter = get_object_or_404(DragonShelterProfile, pk=1)
    paddy_pony = get_object_or_404(PaddyPony, pk=1)
    return render(request, 'paddy_pony.html', {'paddy_pony': paddy_pony, 'dragon_shelter':dragon_shelter})

def serve_logo(request):
    logo_url = "https://www.thedragonshelter.com/static/img/green-logo.png"
    
    return HttpResponseRedirect(logo_url)