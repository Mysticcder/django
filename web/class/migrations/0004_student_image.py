# Generated by Django 5.0.2 on 2024-02-28 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0003_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]