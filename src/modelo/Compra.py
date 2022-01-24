from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
)


class Compra(Model):
    class Meta:
        table_name = 'Compras'

    cliente = UnicodeAttribute(hash_key=True)
    vendedor = UnicodeAttribute(hash_key=True)
    producto = UnicodeAttribute(hash_key=True)
    precio = NumberAttribute()
    fecha = UTCDateTimeAttribute()