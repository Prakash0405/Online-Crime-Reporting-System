# Generated by Django 4.1.6 on 2023-04-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='media/Profile images/default.png', null=True, upload_to='Profile images/'),
        ),
    ]
