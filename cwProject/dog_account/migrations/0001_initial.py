# Generated by Django 2.0.6 on 2019-02-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('realName', models.CharField(max_length=50)),
                ('accountNumber', models.IntegerField(max_length=16)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=99999999999)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
