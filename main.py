import logging
from math import prod

logging.basicConfig(level=logging.INFO)

# input: 
# operation (int) - type of operation defined by number: 1 - addition, 2 - subtraction, 3 - multiplication, 4 -division
# list_of_numbers (list of floats) - list of numbers which will be used in calculation
# output: 
# result of calculation (float/str*)
def calculate(operation, list_of_numbers):
  if operation == 1:
    logging.info(f" Dodaję {' i '.join(str(n) for n in list_of_numbers)}...")
    return sum(list_of_numbers)
  if operation == 2: 
    logging.info(f" Odejmuję {list_of_numbers[1]} od {list_of_numbers[0]}...")
    return list_of_numbers[0] - list_of_numbers[1]
  if operation == 3:
    logging.info(f" Mnożę {' i '.join(str(n) for n in list_of_numbers)}...")
    return prod(list_of_numbers)
  if operation == 4:
    logging.info(f" Dzielę {list_of_numbers[0]} przez {list_of_numbers[1]}...")
    if list_of_numbers[1] == 0:
      logging.warning(' Wykonano dzielenie przez 0.')
      return 'symbol nieoznaczony'
    return list_of_numbers[0]/list_of_numbers[1]
  else:
    logging.error('Źle podana operacja w funkcji calculate.')
    exit(1)
    
print("Witaj w kalkulatorze!")
print("W celu zakończenia programu wciśnij CTRL + D.")
while True:
  try:
    try:
      operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    except ValueError:
      logging.warning(' Operację należy wyrazić liczbą naturalną.')
      continue
    if not operation in range(1,5): 
      logging.warning(' Podano niewłaściwą liczbę. Operację należy wyrazić jako: 1, 2, 3 lub 4. ')
      continue
    if operation%2 == 0: amountofnumbers = 2
    else:
      while True:
        try:
          amountofnumbers = int(input("Podaj ilość liczb, na których chcesz operować: "))
          break
        except ValueError:
          logging.warning(' Podano nieprawidłową ilość liczb. Powinna być ona liczbą naturalną.')
          continue
    while True:
      try:
        list_of_numbers = [float(input(f"Podaj liczbę {n}. ")) for n in range(1,amountofnumbers+1)]
        break
      except ValueError:
        logging.warning(' Podano niewłaściwą liczbę. Obsługiwane są liczby wymierne.')
        continue
    print(f"Wynik to: {calculate(operation, list_of_numbers)}")
  except EOFError:
    print('\nŻegnaj!')
    logging.error('End of file - aplication die.')
    break
