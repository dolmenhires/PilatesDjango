# Generated by Django 2.2.12 on 2020-10-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_auto_20201017_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='yoga_infanti',
        ),
        migrations.AddField(
            model_name='alumno',
            name='yoga_infantil',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='charlas_bebes',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='charlas_educa',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='hipopresivos',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='mamas_bebes',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='mindfulness',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='pago_matricula',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='pilates',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='pilates_infantil',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='taller_meditacion',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='yoga',
            field=models.BooleanField(),
        ),
    ]
