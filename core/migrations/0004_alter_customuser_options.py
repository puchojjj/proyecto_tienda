# Generated by Django 4.2.1 on 2023-07-09 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Usuario personalizado', 'verbose_name_plural': 'Usuarios personalizados'},
        ),
    ]