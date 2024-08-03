from django.urls import path # This allows for the paths to be made 
from . import views # This imports all the information from the urls.py file into here to be used globally

urlpatterns = [
    path('', views.home, name="home"),  # '' in the quotes is the further instructions for the url. views.x follows to a function in views.py
    path('<int:year>/<str:month>', views.home, name="home"), # The <> allows for an arbitrary value to be entered. 
    path('events', views.all_events, name="list_events"), # The name allows for them to be identified later in other files
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venues', views.list_venues, name='list-venues'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('search_venues', views.search_venues, name='search-venues'),
]