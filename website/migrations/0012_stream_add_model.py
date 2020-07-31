# Generated by Django 3.0.3 on 2020-03-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_student_placed'),
    ]

    operations = [
        migrations.CreateModel(
            name='stream_add_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('icon', models.FileField(upload_to='images/')),
            ],
        ),
    ]
