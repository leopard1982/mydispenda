# Generated by Django 4.2.7 on 2023-12-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0013_surattugas_id_nomorsurat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surattugas',
            name='ID_NomorSurat',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
