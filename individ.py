#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список работников.
    trains = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            point = input("Пункт назначения: ")
            number = input("Номер поезда: ")
            time = input("Время отправления: ")

            # Создать словарь.
            train = {
                'point': point,
                'number': number,
                'time': time,
            }

            # Добавить словарь в список.
            trains.append(train)
            # Отсортировать список в случае необходимости.
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 6,
                '-' * 20,
                '-' * 30,
                '-' * 20
            )
            print(line)
            print(
                '| {:^6} | {:^20} | {:^30} | {:^20} |'.format(
                    "№",
                    "Пункт назначения",
                    "Номер поезда",
                    "Время отправления"
                )
            )

            print(line)

            # Вывести данные о всех людях.
            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>6} | {:<20} | {:<30} | {:<20} |'.format(
                        idx,
                        train.get('point', ''),
                        train.get('number', ''),
                        train.get('time', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):
            # Разбить команду на части для выделения Нормера поезда
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый номер поезда
            number_train = parts[1]
            search_train = []

            # Проверить сведения о поездах
            for train in trains:
                if train["number"] == number_train:
                    search_train.append(train)

            if len(search_train) > 0:
                line_new = '+-{}-+-{}-+-{}-+-{}-+'.format(
                    '-' * 6,
                    '-' * 20,
                    '-' * 30,
                    '-' * 20
                )
                print(line_new)

                print(
                    '| {:^6} | {:^20} | {:^30} | {:^20} | '.format(
                        "№",
                        "Пункт назначения",
                        "Номер поезда",
                        "Время отправления"
                    )
                )
                print(line_new)

                for idx_new, spisok_new in enumerate(search_train, 1):
                    print(
                        '| {:>6} | {:<20} | {:<30} | {:<20} | '.format(
                            idx_new,
                            spisok_new.get('point', ''),
                            spisok_new.get('number', ''),
                            spisok_new.get('time', '')
                        )
                    )

                print(line_new)

            else:
                print("Поезда с заданным номером не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить новый поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить данные о поезде;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
