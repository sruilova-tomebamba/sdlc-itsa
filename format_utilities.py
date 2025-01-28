from datetime import datetime

#TODO
def format_date(date, format_type="YYYY-MM-DD"):
   """
    Pendiente de desarrollo
    """

#TODO
def format_currency(amount, currency):
    if currency=="USD":
        Euro=(amount*0.85)
        PesoMX=(amount*19.85)
        return f"EUR: {Euro} MXN: {PesoMX}"
    elif currency=="EUR":
        Dolar=(amount*1.18)
        PesoMX=(amount*23.39)
        return f"USD: {Dolar} MXN: {PesoMX}"
    elif currency=="MXN":
        Dolar=(amount*0.050)
        Euro=(amount*0.043)
        return f"USD: {Dolar} EUR: {Euro}"
    else:
        return "TIPO NO PERMITIDO"

def format_decimal(number, decimal_places=2):
    return f"{number:.{decimal_places}f}"
