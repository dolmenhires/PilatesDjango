# Generated by Django 2.2.12 on 2020-07-06 14:27

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False, verbose_name='_id'),
        ),
    ]
