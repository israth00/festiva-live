# Generated by Django 4.1.5 on 2023-02-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_rename_registerdb_addregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='addregister',
        ),
    ]