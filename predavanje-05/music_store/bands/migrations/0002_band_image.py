# Generated by Django 3.1.5 on 2021-01-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='image',
            field=models.URLField(default='https://m.economictimes.com/thumb/msid-73612807,width-1200,height-900,resizemode-4,imgsize-212384/vinyl-records_istock.jpg'),
        ),
    ]
