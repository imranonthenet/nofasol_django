from django.urls import path
from . import views

app_name = 'event_app'

urlpatterns = [
    path('edit/', views.edit, name='edit'),
    path('event_fields/<int:id>', views.event_fields, name='event_fields'),
    path('badge_categories/<int:id>', views.badge_categories, name='badge_categories'),
    path('badge_layout/<int:id>', views.badge_layout, name='badge_layout')
]
