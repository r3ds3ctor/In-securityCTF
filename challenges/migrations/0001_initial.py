# Generated by Django 3.0.5 on 2020-07-08 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('reward', models.IntegerField(default=0)),
                ('top', models.IntegerField()),
                ('created', models.DateTimeField(verbose_name='created')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('salt', models.CharField(max_length=100)),
                ('created', models.DateTimeField(verbose_name='created')),
            ],
        ),
        migrations.CreateModel(
            name='UserChallenge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('point', models.IntegerField(default=0)),
                ('created', models.DateTimeField(verbose_name='created')),
                ('id_challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.Challenge', unique=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.User', unique=True)),
            ],
        ),
    ]