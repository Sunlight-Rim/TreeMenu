# Generated by Django 3.2.12 on 2023-03-02 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20230301_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Menu Name')),
                ('options', models.JSONField(verbose_name='Options')),
            ],
            options={
                'verbose_name': 'Menus',
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.DeleteModel(
            name='MenuModel',
        ),
    ]
