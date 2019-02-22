from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=264)
    event_from_date = models.DateField()
    event_to_date = models.DateField()

    def __str__(self):
        return str(self.event_name)

class EventField(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=50)
    field_type = models.CharField(max_length=10)
    field_label = models.CharField(max_length=50)
    is_mandatory = models.BooleanField()
    show_in_search = models.BooleanField()
    include_in_search = models.BooleanField()
    show_in_register = models.BooleanField()
    show_in_print = models.BooleanField()
    column_in_excel = models.CharField(max_length=1)
    top = models.IntegerField()
    left = models.IntegerField()
    width = models.IntegerField(default=100)
    font_family = models.CharField(max_length=50, default='Calibri')
    font_size = models.IntegerField(default=11)
    font_weight = models.CharField(max_length=10, default='normal')
    font_style = models.CharField(max_length=10, default='normal')
    text_align = models.CharField(max_length=10, default='left')

    def __str__(self):
        return self.field_name

class BadgeCategory(models.Model):
    code = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.desc

class EventBadgeCategory(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    badge_category_code = models.CharField(max_length=50)
    badge_category_desc = models.CharField(max_length=50)
    show_in_register = models.BooleanField()

    def __str__(self):
        return self.badge_category_desc