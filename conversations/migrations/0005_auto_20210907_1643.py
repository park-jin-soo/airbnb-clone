# Generated by Django 2.2.5 on 2021-09-07 07:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0004_auto_20210907_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(related_name='conversation', to=settings.AUTH_USER_MODEL),
        ),
    ]
