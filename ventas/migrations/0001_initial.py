# Generated by Django 2.2.6 on 2020-05-20 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0002_auto_20200520_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Cliente')),
                ('productos', models.ManyToManyField(to='administracion.Producto')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'venta',
            },
        ),
    ]
