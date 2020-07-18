# Generated by Django 3.0.8 on 2020-07-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingApp', '0004_auto_20200713_2202'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Router',
        ),
        migrations.AddField(
            model_name='report',
            name='specifications',
            field=models.FileField(default='null', upload_to='router_specifications'),
        ),
        migrations.AlterField(
            model_name='report',
            name='Name',
            field=models.CharField(default='null', max_length=2083),
        ),
    ]
