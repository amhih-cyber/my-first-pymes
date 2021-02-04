from django.contrib import admin
from .models import Empresa

admin.site.register(Empresa)

from django.contrib import admin
from .models import Producto

admin.site.register(Producto)


from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)


from django.contrib import admin
from .models import Pedido

admin.site.register(Pedido)


from django.contrib import admin
from .models import TipoComercio

admin.site.register(TipoComercio)
