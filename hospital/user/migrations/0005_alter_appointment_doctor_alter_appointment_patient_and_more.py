# Generated by Django 5.0.4 on 2024-07-05 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='user.doctorreg'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='user.patientreg'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]