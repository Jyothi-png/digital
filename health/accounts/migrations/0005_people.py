# Generated by Django 3.0.4 on 2020-04-07 08:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200406_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('adhar_no', models.IntegerField(null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('img', models.ImageField(null=True, upload_to='certifications')),
            ],
        ),
    ]
