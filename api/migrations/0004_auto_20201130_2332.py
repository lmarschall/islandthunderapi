# Generated by Django 3.1.3 on 2020-11-30 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201130_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='token',
            field=models.CharField(default='', max_length=40),
        ),
    ]