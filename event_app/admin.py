from django.contrib import admin
from event_app.models import Event, EventField, BadgeCategory, EventBadgeCategory
# Register your models here.

admin.site.register(Event)
admin.site.register(EventField)
admin.site.register(BadgeCategory)
admin.site.register(EventBadgeCategory)

