# Generated by Django 3.0.8 on 2020-07-14 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingApp', '0008_auto_20200714_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaunchpadDefects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Defect_Name', models.CharField(default='null', max_length=2083)),
                ('Defect_Severity', models.CharField(default='null', max_length=2083)),
                ('Defect_Priority', models.CharField(default='null', max_length=2083)),
                ('Defect_State', models.CharField(default='null', max_length=2083)),
                ('Defect_Attachements', models.FileField(default='null', upload_to='media')),
            ],
        ),
    ]
