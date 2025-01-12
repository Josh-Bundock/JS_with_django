from django.shortcuts import render 
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from . models import Event, Venue
from . forms import VenueForm  # Imports the class from the form file 
from django.http import HttpResponseRedirect  # Allows for a HTTP response

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']

        return render(request, 'events/search_venues.html', {'searched':searched})
    else:
        return render(request, 'events/search_venues.html', {})

def show_venue(request, venue_id):  # Basic structure hoever the addition of venue_id is the same as what was passed in urls.py into the url
    venue = Venue.objects.get(pk=venue_id)  # pk stands for primary key which will allocate a number to the venue_id
    return render(request, 'events/show_venue.html', {'venue': venue})  

def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venues.html', {'venue_list': venue_list})  # Used in html files to indentify the function in views.py

def add_venue(request):  
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {"event_list": event_list})  

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.title()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    # Create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # Get current year
    now = datetime.now()
    current_year = now.year

    # Get current time
    time = now.strftime('%H:%M %p')

    return render(request, 'events/home.html', {"year": year, "month": month, "month_number": month_number, 
    "cal": cal, "current_year": current_year, "time": time})
