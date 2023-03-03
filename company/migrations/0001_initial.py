# Generated by Django 4.1.7 on 2023-03-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
            },
        ),
    ]