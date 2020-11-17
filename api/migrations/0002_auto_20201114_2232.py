# Generated by Django 3.0.8 on 2020-11-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='group',
            field=models.CharField(choices=[('U', 'Undergraduate'), ('G', 'Graduate'), ('P', 'Professor')], max_length=10),
        ),
    ]
