# Generated by Django 4.2.7 on 2023-12-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='portfolio/images/default_image.jpg', upload_to='portfolio/images/'),
        ),
    ]