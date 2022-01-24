import Usuario


class Vendedor(Usuario, discriminator='vendedor'):
    class Meta:
        table_name = 'Vendedores'

