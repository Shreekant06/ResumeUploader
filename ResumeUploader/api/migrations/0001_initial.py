# Generated by Django 4.2.4 on 2023-08-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('Bihar', 'Bihar'), ('West Bengal', 'West Bengal'), ('Gujarat', 'Gujarat'), ('Maharashtra', 'Maharashtra'), ('Goa', 'Goa'), ('Delhi', 'Delhi')], max_length=50)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pimg', models.ImageField(blank=True, upload_to='pimages')),
                ('docs', models.FileField(blank=True, upload_to='documents')),
            ],
        ),
    ]