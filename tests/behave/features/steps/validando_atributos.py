@when(u'um cliente investir o capital inicial de {capital_inicial:f} durante um período de 2 meses com uma rentabilidade de 6% ao mês.')
def capital_inicial(context, capital_inicial):
    context.capital_inicial = context.capital_inicial

@then(u'seu capital inicial deve ser {capital_inicial:f}')
def checar_capital_inicial(context, capital_inicial):
    assert context.capital_inicial == capital_inicial
