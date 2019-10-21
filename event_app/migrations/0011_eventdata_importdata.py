# Generated by Django 2.1.5 on 2019-03-16 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0010_auto_20190316_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('firstName', models.CharField(max_length=255)),
                ('middleName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('fullName', models.CharField(max_length=255)),
                ('jobTitle', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('companyName', models.CharField(max_length=255)),
                ('mobile1', models.CharField(max_length=255)),
                ('mobile2', models.CharField(max_length=255)),
                ('tel1', models.CharField(max_length=255)),
                ('tel2', models.CharField(max_length=255)),
                ('fax', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('poBox', models.CharField(max_length=255)),
                ('postalCode', models.CharField(max_length=255)),
                ('badgeCategory', models.CharField(max_length=255)),
                ('regType', models.CharField(max_length=255)),
                ('regDate', models.CharField(max_length=255)),
                ('badgePrintDate', models.CharField(max_length=255)),
                ('modifiedDate', models.CharField(max_length=255)),
                ('statusFlag', models.CharField(max_length=255)),
                ('backoffice', models.CharField(max_length=255)),
                ('comment1', models.CharField(max_length=255)),
                ('comment2', models.CharField(max_length=255)),
                ('comment3', models.CharField(max_length=255)),
                ('comment4', models.CharField(max_length=255)),
                ('comment5', models.CharField(max_length=255)),
                ('comment6', models.CharField(max_length=255)),
                ('comment7', models.CharField(max_length=255)),
                ('comment8', models.CharField(max_length=255)),
                ('comment9', models.CharField(max_length=255)),
                ('comment10', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='ImportData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_file', models.FileField(upload_to='imports')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.Event')),
            ],
        ),
    ]