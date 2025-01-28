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




def calculate_days(fech_ini, fech_fin):
    fecha_inicio = datetime.strptime(fech_ini, "%d/%m/%Y")
    fecha_final = datetime.strptime(fech_fin, "%d/%m/%Y")

    diferencia_dias = fecha_final - fecha_inicio
    
    return abs(diferencia_dias.days)