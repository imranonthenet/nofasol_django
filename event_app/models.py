from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_logo = models.FileField(upload_to='images')
    event_from_date = models.DateField()
    event_to_date = models.DateField()
    setup_complete = models.BooleanField()

    def __str__(self):
        return str(self.event_name)

class ImportData(models.Model):
    import_file = models.FileField(upload_to='imports')


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

class EventData(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    middleName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    fullName = models.CharField(max_length=255)
    jobTitle = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    mobile1 = models.CharField(max_length=255)
    mobile2 = models.CharField(max_length=255)
    tel1 = models.CharField(max_length=255)
    tel2 = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    poBox = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    badgeCategory= models.CharField(max_length=255)
    regType = models.CharField(max_length=255)
    regDate = models.CharField(max_length=255)
    badgePrintDate = models.CharField(max_length=255)
    modifiedDate = models.CharField(max_length=255)
    statusFlag = models.CharField(max_length=255)
    backoffice = models.CharField(max_length=255)
    comment1 = models.CharField(max_length=255)
    comment2 = models.CharField(max_length=255)
    comment3 = models.CharField(max_length=255)
    comment4 = models.CharField(max_length=255)
    comment5 = models.CharField(max_length=255)
    comment6 = models.CharField(max_length=255)
    comment7 = models.CharField(max_length=255)
    comment8 = models.CharField(max_length=255)
    comment9 = models.CharField(max_length=255)
    comment10 = models.CharField(max_length=255)
    username = models.CharField(max_length=255)