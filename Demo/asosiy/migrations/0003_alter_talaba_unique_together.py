# Generated by Django 4.2 on 2023-04-14 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_alter_talaba_ism'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='talaba',
            unique_together={('ism', 'email')},
        ),
    ]
