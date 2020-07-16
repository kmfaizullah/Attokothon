# Generated by Django 3.0.8 on 2020-07-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bestPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('post', models.CharField(max_length=5000)),
                ('date', models.CharField(max_length=15)),
                ('keypoints', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('post', models.CharField(max_length=5000)),
                ('date', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('post', models.CharField(max_length=5000)),
                ('date', models.CharField(max_length=15)),
                ('note', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('user_name', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=150)),
                ('place', models.CharField(max_length=5000)),
                ('date', models.CharField(max_length=15)),
                ('note', models.CharField(max_length=1000)),
            ],
        ),
    ]