# Generated by Django 4.1.5 on 2023-02-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('confirm_password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
