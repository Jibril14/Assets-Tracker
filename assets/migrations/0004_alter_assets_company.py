# Generated by Django 4.1.7 on 2023-03-04 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('assets', '0003_alter_assets_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='company',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
