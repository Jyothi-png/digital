# Generated by Django 3.0.4 on 2020-04-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_people_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_num', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('drug_name', models.CharField(max_length=50, null=True)),
                ('dose', models.CharField(max_length=50, null=True)),
                ('quantity', models.CharField(max_length=50, null=True)),
                ('slots', models.CharField(max_length=50, null=True)),
                ('time', models.CharField(max_length=50, null=True)),
                ('preferred', models.CharField(max_length=50, null=True)),
                ('note', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_num', models.IntegerField(null=True)),
                ('BP', models.CharField(max_length=50, null=True)),
                ('temperature', models.CharField(max_length=50, null=True)),
                ('pulse_rate', models.CharField(max_length=50, null=True)),
                ('height', models.CharField(max_length=50, null=True)),
                ('weight', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
