# Generated by Django 3.0.3 on 2020-03-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200304_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='events_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=225)),
                ('event_desc', models.TextField()),
            ],
        ),
    ]
