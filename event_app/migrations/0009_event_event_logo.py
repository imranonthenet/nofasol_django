# Generated by Django 2.1.5 on 2019-03-16 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0008_event_setup_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_logo',
            field=models.CharField(default=1, max_length=264),
            preserve_default=False,
        ),
    ]
