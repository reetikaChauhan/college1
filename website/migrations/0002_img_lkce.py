# Generated by Django 3.0.3 on 2020-03-01 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img_lkce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lkce_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
