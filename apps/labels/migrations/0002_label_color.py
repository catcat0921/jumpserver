# Generated by Django 4.1.13 on 2024-06-04 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="label",
            name="color",
            field=models.CharField(
                blank=True, default="", max_length=32, verbose_name="Color"
            ),
        ),
        migrations.AlterField(
            model_name="labeledresource",
            name="label",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="labeled_resources",
                to="labels.label",
                verbose_name="Tag",
            ),
        ),
    ]
