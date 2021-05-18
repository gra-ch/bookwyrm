# Generated by Django 3.2 on 2021-05-17 19:02

import bookwyrm.models.fields
from django.db import migrations


def forward_func(apps, schema_editor):
    """set the generated note types"""
    db_alias = schema_editor.connection.alias

    generated_notes = apps.get_model("bookwyrm", "GeneratedNote").objects.using(
        db_alias
    )

    for note in generated_notes:
        if "started" in note.content:
            note.note_type = "READING"
        elif "finished" in note.content:
            note.note_type = "READ"
        elif "wants" in note.content:
            note.note_type = "TO_READ"
        else:
            note.note_type = "GOAL"
        note.save()


def reverse_func(apps, schema_editor):
    """nothing to do here"""


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0073_sitesettings_footer_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="generatednote",
            name="note_type",
            field=bookwyrm.models.fields.CharField(
                choices=[
                    ("TO_READ", "To Read"),
                    ("READING", "Reading"),
                    ("READ", "Read"),
                    ("GOAL", "Goal"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.RunPython(forward_func, reverse_func),
        migrations.AlterField(
            model_name="generatednote",
            name="note_type",
            field=bookwyrm.models.fields.CharField(
                choices=[
                    ("TO_READ", "To Read"),
                    ("READING", "Reading"),
                    ("READ", "Read"),
                    ("GOAL", "Goal"),
                ],
                max_length=255,
            ),
        ),
    ]