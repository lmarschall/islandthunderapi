# Generated by Django 3.1.3 on 2020-11-30 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('uid', models.CharField(default='', max_length=64)),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
                'db_table': 'api_players',
            },
        ),
        migrations.CreateModel(
            name='MyOwnToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to='api.player', verbose_name='Player')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
            },
        ),
    ]
