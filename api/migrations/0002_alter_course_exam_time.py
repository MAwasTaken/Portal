# Generated by Django 4.1.7 on 2023-02-17 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='exam_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.time'),
        ),
    ]
