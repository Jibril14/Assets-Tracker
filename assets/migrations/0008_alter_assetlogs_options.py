# Generated by Django 4.1.7 on 2023-03-04 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_alter_assetlogs_check_out'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assetlogs',
            options={'ordering': ['asset'], 'verbose_name': 'assets_log', 'verbose_name_plural': 'assets_logs'},
        ),
    ]
