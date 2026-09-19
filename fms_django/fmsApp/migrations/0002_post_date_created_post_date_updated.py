"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("fmsApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="date_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="post",
            name="date_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
