import format_utilities as fu

def main():
  # Invocar format_currency
  print(fu.format_currency(123456.789, "USD"))

  # Invocar format_decimal
  print(fu.format_decimal(123456.789, 2))

  # Invocar format_date
  print(fu.format_date("2023-12-31", format_type="%d/%m/%Y"))

  # Invocar calculate_days
  print(fu.calculate_days("01/01/2023", "31/12/2023"))

if __name__ == "__main__":
  main()