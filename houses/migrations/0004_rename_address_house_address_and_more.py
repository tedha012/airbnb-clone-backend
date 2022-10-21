# Generated by Django 4.1.2 on 2022-10-21 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_house_pet_allowed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='Address',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='house',
            name='pet_allowed',
        ),
        migrations.AddField(
            model_name='house',
            name='pets_allowed',
            field=models.BooleanField(default=True, help_text='Does this house allow pets?', verbose_name='Pets Allowed?'),
        ),
        migrations.AlterField(
            model_name='house',
            name='price_per_night',
            field=models.PositiveIntegerField(help_text='Positive Numbers Only', verbose_name='Price'),
        ),
    ]
