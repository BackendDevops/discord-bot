# Generated by Django 2.2.6 on 2019-11-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standup', '0012_auto_20191103_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='standup',
            name='standup_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
