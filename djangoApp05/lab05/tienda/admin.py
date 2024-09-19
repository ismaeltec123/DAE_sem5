from django.contrib import admin

# Register your models here.

from .models import Categoria
from .models import Producto
from .models import Cliente


def igualar_stock(modeladmin, request, queryset):
    for producto in queryset:
        producto.stock = 20  # Aumenta el stock en 10 (puedes ajustar este valor según tu lógica)
        producto.save()
    modeladmin.message_user(request, "El stock de los productos quedo en 20.")

igualar_stock.short_description = "Igualar stock de productos a 20 unidades"

class ProductosAdmin(admin.ModelAdmin):
    list_display=('nombre','stock')
    actions=[igualar_stock]

admin.site.register(Categoria)
admin.site.register(Producto,ProductosAdmin)
admin.site.register(Cliente)