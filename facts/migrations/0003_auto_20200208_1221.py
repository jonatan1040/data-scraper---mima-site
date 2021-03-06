# Generated by Django 3.0.3 on 2020-02-08 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0002_auto_20200205_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='facts',
            name='author',
            field=models.CharField(default='none', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='facts',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='facts', to='facts.Song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='songs', to='facts.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.CharField(default='none', max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
