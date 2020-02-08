# Generated by Django 3.0.3 on 2020-02-05 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facts',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='facts.Song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='facts.Artist'),
        ),
    ]
