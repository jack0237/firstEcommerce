# Generated by Django 4.1.4 on 2022-12-19 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daily_food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='daily_food.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=500000),
        ),
    ]