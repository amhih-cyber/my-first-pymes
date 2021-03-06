# Generated by Django 2.2.17 on 2021-01-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pymes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('teléfono', models.CharField(max_length=30)),
                ('dirección', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('ubicación', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('CIF', models.CharField(max_length=15)),
                ('teléfono', models.CharField(max_length=30)),
                ('dirección', models.CharField(max_length=150)),
                ('tipoComercio', models.CharField(max_length=100)),
                ('ubicación', models.TextField()),
                ('añoIncorporación', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripción', models.CharField(max_length=30)),
                ('cliente', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PedidosProductos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.IntegerField()),
                ('producto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipoProducto', models.CharField(max_length=100)),
                ('tamañao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoComercio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripción', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tipoproducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
