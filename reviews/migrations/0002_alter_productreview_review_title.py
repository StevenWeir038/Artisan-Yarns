# Generated by Django 3.2 on 2022-07-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='review_title',
            field=models.CharField(max_length=254),
        ),
    ]
