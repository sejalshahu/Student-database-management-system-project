# Generated by Django 5.0.1 on 2024-02-15 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacollection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='intime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='outtime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='joiningdate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='rollno',
            field=models.IntegerField(),
        ),
    ]
