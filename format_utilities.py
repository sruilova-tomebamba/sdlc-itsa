from datetime import datetime

#TODO
def format_date(date):
   
    fecha_formato_uno = date.strftime('%Y-%m-%d')
    print("Formato 1 YYYY-MM-DD:",fecha_formato_uno)

    fecha_formato_dos = date.strftime('%d/%m/%Y')
    print("Formato 2 DD-MM-YYYY:",fecha_formato_dos)    

    fecha_formato_tres = date.strftime('%m/%d/%Y')
    print("Formato 2 DD-MM-YYYY:",fecha_formato_tres)    
   
    return 
#TODO
def format_currency(amount, currency="USD"):
    """
    Pendiente de desarrollo
    """



def format_decimal(number, decimal_places=2):
    return f"{number:.{decimal_places}f}"


date = datetime.now()
format_date(date)