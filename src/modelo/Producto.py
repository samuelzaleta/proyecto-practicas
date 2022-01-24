from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, UnicodeSetAttribute, NumberAttribute
)


class Producto(Model):
    class Meta:
        table_name = 'Productos'

    nombre = UnicodeAttribute(hash_key=True)
    precio = NumberAttribute()
    categorias = UnicodeSetAttribute()


