from django.urls import path
from . import views

app_name = 'event_app'

urlpatterns = [
    path('event_list/', views.event_list, name='event_list'),
    path('create_event', views.create_event, name='create_event'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('event_fields/<int:id>', views.event_fields, name='event_fields'),
    path('badge_categories/<int:id>', views.badge_categories, name='badge_categories'),
    path('badge_layout/<int:id>', views.badge_layout, name='badge_layout'),
    path('import_data/<int:id>', views.import_data, name='import_data'),
]


