# Generated by Django 3.2.9 on 2021-12-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psicologo', '0002_alter_professional_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
