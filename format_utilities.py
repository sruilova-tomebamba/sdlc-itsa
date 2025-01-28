from datetime import datetime
import sys

#TODO
def format_date(date, format_type="YYYY-MM-DD"):
   """
    Pendiente de desarrollo
    """

#TODO
def format_currency(amount, currency):
    if currency=="USD":
        Euro=(amount*0.95)
        PesoMX=(amount*20.55)
        return f"EUR: {Euro} MXN: {PesoMX}"
    elif currency=="EUR":
        Dolar=(amount*1.04)
        PesoMX=(amount*21.43)
        return f"USD: {Dolar} MXN: {PesoMX}"
    elif currency=="MXN":
        Dolar=(amount*0.050)
        Euro=(amount*0.047)
        return f"USD: {Dolar} EUR: {Euro}"
    else:
        return "TIPO NO PERMITIDO"

def format_decimal(number, decimal_places=2):
    return f"{number:.{decimal_places}f}"
