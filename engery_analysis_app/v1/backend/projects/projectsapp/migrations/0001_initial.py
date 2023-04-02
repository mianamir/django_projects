# Generated by Django 4.1.7 on 2023-03-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=100, null=True)),
                ('project_number', models.CharField(blank=True, max_length=100, null=True)),
                ('acquisition_date', models.EmailField(blank=True, max_length=100, null=True)),
                ('number_3l_code', models.EmailField(blank=True, max_length=100, null=True)),
                ('project_deal_type_id', models.EmailField(blank=True, max_length=100, null=True)),
                ('project_group_id', models.EmailField(blank=True, max_length=100, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'projects',
            },
        ),
    ]