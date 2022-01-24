from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, DiscriminatorAttribute
)


class Usuario(Model):
    class Meta:
        table_name = 'Usuarios'

    correo = UnicodeAttribute(hash_key=True)
    nombre = UnicodeAttribute()
    contrasenia = UnicodeAttribute()
    tipo = DiscriminatorAttribute()
