# Generated by Django 4.1 on 2023-10-01 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cook',
            options={'verbose_name': 'cook', 'verbose_name_plural': 'cooks'},
        ),
        migrations.AddField(
            model_name='cook',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='photos/cooks'),
        ),
        migrations.AddField(
            model_name='dish',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='photos/dishes'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='restaurant.dishtype'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='dishtype',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
