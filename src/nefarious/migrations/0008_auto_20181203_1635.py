# Generated by Django 2.1.1 on 2018-12-03 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0007_auto_20181203_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchmovie',
            old_name='quality_profile',
            new_name='quality_profile_custom',
        ),
        migrations.RenameField(
            model_name='watchtvepisode',
            old_name='quality_profile',
            new_name='quality_profile_custom',
        ),
        migrations.RenameField(
            model_name='watchtvshow',
            old_name='quality_profile',
            new_name='quality_profile_custom',
        ),
    ]