# Generated by Django 4.1.7 on 2023-03-04 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assets.category'),
        ),
    ]