# Generated by Django 4.2.13 on 2024-07-19 13:58

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0007_session_hall'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='session',
            name='hall',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cinema', chained_model_field='cinema', default=None, on_delete=django.db.models.deletion.CASCADE, to='cinemas.hall', verbose_name='Зал'),
        ),
    ]
