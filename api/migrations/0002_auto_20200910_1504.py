# Generated by Django 2.2.6 on 2020-09-10 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.room'),
        ),
    ]