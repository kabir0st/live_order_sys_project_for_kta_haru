# Generated by Django 2.2 on 2019-05-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20190514_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=50)),
            ],
        ),
    ]
