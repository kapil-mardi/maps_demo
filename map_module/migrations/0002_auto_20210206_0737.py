# Generated by Django 3.1.6 on 2021-02-06 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='district_category', to='map_module.category'),
        ),
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_state', to='map_module.state'),
        ),
    ]
