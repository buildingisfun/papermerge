# Generated by Django 3.0.2 on 2020-04-19 07:46

from django.db import migrations
from papermerge.core.lib.lang import LANG_DICT


def insert_language_maps(apps, schema_editor):
    LanguageMap = apps.get_model('core', 'LanguageMap')
    for key, value in LANG_DICT.items():
        lang_map = LanguageMap(
            tsr_code=key,
            pg_short=value,
            pg_catalog=f"pg_catalog.{value}"
        )
        lang_map.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_languagemap'),
    ]

    operations = [
        migrations.RunPython(insert_language_maps),
    ]
