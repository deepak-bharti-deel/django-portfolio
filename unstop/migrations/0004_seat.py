# Generated by Django 3.0.6 on 2023-10-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unstop', '0003_auto_20231008_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=1)),
                ('seat_number', models.IntegerField()),
            ],
        ),
    ]