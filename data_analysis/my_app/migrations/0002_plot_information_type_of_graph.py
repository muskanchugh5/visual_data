# Generated by Django 2.1.1 on 2018-09-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot_information',
            name='type_of_graph',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
