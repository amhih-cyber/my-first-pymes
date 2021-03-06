# Generated by Django 2.2.17 on 2021-02-04 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pymes', '0002_auto_20210128_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripción', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tamaño', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Pedidos',
        ),
        migrations.DeleteModel(
            name='PedidosProductos',
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
        migrations.RenameField(
            model_name='tipoproducto',
            old_name='descripcion',
            new_name='descripción',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='tipoComercio',
        ),
        migrations.AddField(
            model_name='empresa',
            name='tipocomercio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pymes.TipoComercio'),
            preserve_default=False,
        ),
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
        migrations.AddField(
            model_name='producto',
            name='tipoproducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pymes.TipoProducto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pymes.Cliente'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(to='pymes.Producto'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='producto',
            field=models.ManyToManyField(to='pymes.Producto'),
        ),
    ]
