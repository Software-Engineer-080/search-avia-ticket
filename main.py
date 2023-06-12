flight = ''


# Проверка корректности вводимых данных

def verify_flight(number):
    count = 0

    for string in number:
        count += 1

    return count


def verify_float(number):
    count = True

    if float(number):
        count = True

    else:
        count = False

    return count


def verify_second_number(duration_parameter):
    count = 0
    for digit in duration_parameter:
        if digit == '.':
            return count
        count += 1


def verify_big_zero(ticket_price_parameter):
    flag = True
    for count in ticket_price_parameter:
        if (count == '-') or (ticket_price_parameter == '0'):
            flag = False
        return flag


def ticket_splitting(flight):
    ticket = ''
    for digit_number in flight:
        if digit_number == '!':
            print('Информация о рейсе: ' + ticket)
            ticket = ''
        else:
            ticket += digit_number
    print()


def save_ticket(flight: str, string: str):
    return flight + string + ' '


# Ввод данных о рейсе

def input_flight(flight):
    print()
    print('Введите данные рейса:')

    # Данные о номере рейса

    number_flight_parameter = input('XXXX - номер рейса: ').upper()
    counter = verify_flight(number_flight_parameter)

    while counter != 4:
        print('Введите корректный номер рейса!')
        number_flight_parameter = input('XXXX - номер рейса: ').upper()
        counter = verify_flight(number_flight_parameter)

    flight = save_ticket(flight, number_flight_parameter)

    # Данные о дате рейса

    date_flight_parameter = input('ДД/ММ/ГГГГ - дата рейса: ')
    counter = verify_flight(date_flight_parameter)

    while counter != 10:
        print('Введите корректную дату рейса!')
        date_flight_parameter = input('ДД/ММ/ГГГГ - дата рейса: ')
        counter = verify_flight(date_flight_parameter)

    flight = save_ticket(flight, date_flight_parameter)

    # Данные о времени вылета

    time_flight_parameter = input('ЧЧ:ММ - время вылета: ')
    counter = verify_flight(time_flight_parameter)

    while counter != 5:
        print('Введите корректное время вылета!')
        time_flight_parameter = input('ЧЧ:ММ - время вылета: ')
        counter = verify_flight(time_flight_parameter)

    flight = save_ticket(flight, time_flight_parameter)

    # Данные о длительности перелета

    duration_flight_parameter = input('XX.XX - длительность перелета: ')
    counter_ticket = verify_float(duration_flight_parameter)

    while not counter_ticket:
        print('Введите корректную длительность перелета!')
        duration_flight_parameter = input('XX.XX - длительность перелета: ')
        counter_ticket = verify_float(duration_flight_parameter)

    numbers = verify_second_number(duration_flight_parameter)
    while numbers != 2:
        print('Значение часа должно быть двухзначным!')
        duration_flight_parameter = input('XX.XX - длительность перелета: ')
        numbers = verify_second_number(duration_flight_parameter)

    flight = save_ticket(flight, duration_flight_parameter)

    # Данные об аэропорте вылета

    departure_airport_parameter = input('XXX - аэропорт вылета: ').upper()
    counter = verify_flight(departure_airport_parameter)

    while counter != 3:
        print('Аэропорт вылета должен содержать 3 символа!')
        departure_airport_parameter = input('XXX - аэропорт вылета: ').upper()
        counter = verify_flight(departure_airport_parameter)

    flight = save_ticket(flight, departure_airport_parameter)

    # Данные об аэропорте назначения

    destination_airport_parameter = input('XXX - аэропорт назначения: ').upper()
    counter = verify_flight(destination_airport_parameter)

    while counter != 3:
        print('Аэропорт назначения должен содержать 3 символа!')
        destination_airport_parameter = input('XXX - аэропорт назначения: ').upper()
        counter = verify_flight(destination_airport_parameter)

    flight = save_ticket(flight, destination_airport_parameter)

    # Данные о стоимости билета

    ticket_price_parameter = input('.XX - стоимость билета (>0): ')
    counter_ticket = verify_float(ticket_price_parameter)

    if counter_ticket:
        ticket = verify_big_zero(ticket_price_parameter)
        while not ticket:
            print('Стоимость билета должна быть больше 0!')
            ticket_price_parameter = input('.XX - стоимость билета (>0): ')
            ticket = verify_big_zero(ticket_price_parameter)

    else:

        while not counter_ticket:
            print('Введите корректную стоимость билета!')
            ticket_price_parameter = input('.XX - стоимость билета (>0): ')
            counter_ticket = verify_float(ticket_price_parameter)

    flight = save_ticket(flight, ticket_price_parameter)

    flight += '!'

    # Кампановка всех данных о рейсе

    print()
    print(
        f'Информация о рейсе {number_flight_parameter} {date_flight_parameter} {time_flight_parameter} {duration_flight_parameter} '
        f'{departure_airport_parameter} {destination_airport_parameter} {ticket_price_parameter} добавлена''\n\n')

    main_menu(flight)


# Вывод всех авиабилетов

def output_all_flight(flight):
    if flight == '':
        print('Информация о рейсах отсутствует''\n')
        main_menu(flight)
    else:
        ticket_splitting(flight)
        main_menu(flight)


# Вывод конкретного авиабилета

def search_flight_number(flight):
    number = input('Введите номер рейса в фориате XXXX: ').upper()
    counter = verify_flight(number)

    while counter != 4:
        print('Введите корректный номер рейса!')
        number = input('Введите номер рейса в фориате XXXX: ').upper()
        counter = verify_flight(number)

    found_flight = False
    flight_info = ''
    for flight_str in flight.split("!"):
        if flight_str.startswith(number):
            found_flight = True
            flight_info = flight_str
            break

    if found_flight:
        print('Информация о рейсе: ' + flight_info)
        print()
    else:
        print(f'Рейс {number} не найден\n')

    main_menu(flight)


# Проверка корректности ввода номера меню

def verify_number(flight, number):
    if number == 1:
        input_flight(flight)

    elif number == 2:
        output_all_flight(flight)

    elif number == 3:
        search_flight_number(flight)

    elif number == 0:
        print()
        print('Завершение работы программы!')

    else:
        print('Введите корректный пункт меню!''\n')
        main_menu(flight)


# Главное меню

def main_menu(flight):
    print('Главное меню''\n')
    print('1 - ввод рейса')
    print('2 - вывод всех рейсов')
    print('3 - поиск рейса по номеру')
    print('0 - завершение работы''\n')

    number_menu = int(input('Введите номер пункта меню: '))

    verify_number(flight, number_menu)


print('Сервис поиска авиабилетов''\n''\n')

main_menu(flight)
