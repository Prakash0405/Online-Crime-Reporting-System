# Generated by Django 4.1.6 on 2023-04-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0008_alter_complaint_master_delay_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint_master',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='crime_category_master',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
