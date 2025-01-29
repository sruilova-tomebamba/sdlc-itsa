from datetime import datetime
import sys

#TODO
def format_date(date,b=None, format_type='%Y-%m-%d'):

    if not format_type in ['%d/%m/%Y','%m/%d/%Y']:
        return date.strftime('%Y-%m-%d')
    return date.strftime(format_type)    


#TODO
def format_currency(amount, currency = 'USD'):
    if currency=="USD":
        euro=(amount*0.95)
        peso_mx=(amount*20.55)
        return f"EUR: {euro} MXN: {peso_mx}"
    elif currency=="EUR":
        dolar=(amount*1.04)
        peso_mx=(amount*21.43)
        return f"USD: {dolar} MXN: {peso_mx}"
    elif currency=="MXN":
        dolar=(amount*0.050)
        euro=(amount*0.047)
        return f"USD: {dolar} EUR: {euro}"
    else:
        return "TIPO NO PERMITIDO"

def format_decimal(number, decimal_places=2):
    return f"{number:.{decimal_places}f}"




def calculate_days(fech_ini, fech_fin):
    fecha_inicio = datetime.strptime(fech_ini, "%d/%m/%Y")
    fecha_final = datetime.strptime(fech_fin, "%d/%m/%Y")

    diferencia_dias = fecha_final - fecha_inicio
    
    return abs(diferencia_dias.days)