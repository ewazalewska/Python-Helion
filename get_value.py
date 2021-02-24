def get_value(prompt, value_min, value_max):
    a=True
    while a:
        number_tekst=input(prompt)
        try:
            number=int(number_tekst)
        except ValueError:
            print('Nieprawidłowy symbol, wprowadź liczby')
            continue
        if number < value_min:
            print('Wartość poza zakresem')
            continue
        if number > value_max:
            print('Wartość poza zakresem')
            continue
        a=False
    return number

ride_number=get_value('podaj liczbę z zakresu od 3 do 10 ',3,10)
print('Wybrano numer:',ride_number)
