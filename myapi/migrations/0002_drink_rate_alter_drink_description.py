# Generated by Django 4.2.4 on 2023-12-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='rate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='drink',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
