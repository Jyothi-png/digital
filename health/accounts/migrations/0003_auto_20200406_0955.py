# Generated by Django 3.0.4 on 2020-04-06 04:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_doctor_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('adhar_num', models.IntegerField(null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('img', models.ImageField(null=True, upload_to='certifications')),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='username',
        ),
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='adhar_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='doctor',
            name='qualification',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
