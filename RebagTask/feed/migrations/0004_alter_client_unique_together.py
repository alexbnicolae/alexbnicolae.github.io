# Generated by Django 4.0.3 on 2022-03-07 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_alter_client_email_alter_client_username_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='client',
            unique_together=set(),
        ),
    ]