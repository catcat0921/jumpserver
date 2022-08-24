# Generated by Django 3.1.14 on 2022-04-07 09:26

from django.db import migrations, models


def migrate_platform_type_to_lower(apps, *args):
    platform_model = apps.get_model('assets', 'Platform')
    platforms = platform_model.objects.all()
    for p in platforms:
        p.type = p.type.lower()
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0096_auto_20220406_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platform',
            old_name='base',
            new_name='type',
        ),
        migrations.AddField(
            model_name='platform',
            name='category',
            field=models.CharField(default='host', max_length=16, verbose_name='Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='platform',
            name='type',
            field=models.CharField(default='linux', max_length=32, verbose_name='Type'),
        ),
        migrations.RunPython(migrate_platform_type_to_lower)
    ]
