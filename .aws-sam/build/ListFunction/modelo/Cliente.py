import Usuario


class Cliente(Usuario, discriminator='clientes'):
    class Meta:
        table_name = 'Clientes'
