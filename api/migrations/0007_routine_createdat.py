# Generated by Django 3.0.8 on 2020-10-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200930_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
