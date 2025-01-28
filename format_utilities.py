from datetime import datetime

#TODO
def format_date(date,b=None, format_type='%Y-%m-%d'):

    if not format_type in ['%d/%m/%Y','%m/%d/%Y']:
        return date.strftime('%Y-%m-%d')
    return date.strftime(format_type)    


#TODO
def format_currency(amount, currency="USD"):
    """
    Pendiente de desarrollo
    """



def format_decimal(number, decimal_places=2):
    return f"{number:.{decimal_places}f}"


date = datetime.now()
fecha_formato_uno = format_date(date=date, format_type='%dfsdfY', b=1)
print(fecha_formato_uno)