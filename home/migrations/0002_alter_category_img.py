# Generated by Django 5.0.4 on 2024-04-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(default='category.jpg', upload_to='Category'),
        ),
    ]