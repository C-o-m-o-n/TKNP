# Generated by Django 2.2 on 2019-08-24 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clearance', '0002_auto_20190822_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='hod',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
