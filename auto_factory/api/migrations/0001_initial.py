# Generated by Django 2.2.16 on 2022-07-05 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prime_cost', models.FloatField(verbose_name='Себестоимость машины')),
                ('margin', models.CharField(max_length=20, verbose_name='Наценка')),
                ('finall_price', models.FloatField(verbose_name='Финальная стоимость изделия')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=40, unique=True, verbose_name='Тип детали')),
                ('price', models.FloatField(verbose_name='Стоимость детали')),
                ('amount', models.IntegerField(verbose_name='Количество деталей на одну машину')),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование параметра')),
                ('value', models.CharField(max_length=50, verbose_name='Значение параметра')),
            ],
        ),
        migrations.CreateModel(
            name='DetailParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Detail')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Parameter')),
            ],
        ),
        migrations.AddField(
            model_name='detail',
            name='parameters',
            field=models.ManyToManyField(through='api.DetailParameter', to='api.Parameter'),
        ),
    ]
