from cliente import Cliente


def before_feature(context, feature):
    cliente = Cliente(capital_inicial=5000)
    context.capital_inicial = cliente.pega_capital_inicial()
