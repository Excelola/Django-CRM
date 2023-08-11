# Generated by Django 4.2.3 on 2023-08-09 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.DateTimeField(max_length=50)),
                ('last_name', models.DateTimeField(max_length=50)),
                ('email', models.DateTimeField(max_length=100)),
                ('phone', models.DateTimeField(max_length=15)),
                ('address', models.DateTimeField(max_length=100)),
                ('city', models.DateTimeField(max_length=50)),
                ('state', models.DateTimeField(max_length=50)),
                ('zipcode', models.DateTimeField(max_length=20)),
            ],
        ),
    ]