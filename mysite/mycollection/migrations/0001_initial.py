# Generated by Django 4.2.7 on 2023-11-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=200)),
                ('modele', models.CharField(max_length=200)),
                ('prix', models.IntegerField()),
                ('coloris', models.CharField(max_length=50)),
            ],
        ),
    ]
