# Generated by Django 3.0.3 on 2020-05-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_academic_calender'),
    ]

    operations = [
        migrations.CreateModel(
            name='information_model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_info', models.CharField(max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('info', models.TextField()),
                ('heading', models.TextField()),
            ],
        ),
    ]
