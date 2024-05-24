def main():
    # Инициализация списка для хранения чисел
    numbers = []

    # Вывод приглашения к вводу чисел
    print("Введите числа (для завершения введите 'stop') -> ")

    # Цикл для сбора чисел от пользователя
    while True:
        # Получение ввода от пользователя
        input_num = input()

        # Проверка на ввод "stop" для завершения ввода
        if input_num == "stop":
            break

        # Проверка на пустой ввод
        if input_num == "":
            print("Введите число или 'stop' -> ")
            continue

        # Попытка преобразовать введенное значение в целое число
        try:
            number = int(input_num)
            # Добавление числа в список
            numbers.append(number)
        # Обработка исключения ValueError при ошибке преобразования
        except:
            print("Некорректный ввод!")

    # Вычисление суммы чисел
    result_sum = sum(numbers)
    # Инициализация произведения чисел 
    result_mul = 1
    # Инициализация разности чисел (первое число - остальные)
    result_sub = numbers[0]
    # Инициализация частного чисел (первое число / остальные)
    result_div = numbers[0]

    # Вычисление произведения чисел
    for num in numbers:
        result_mul *= num

    # Вычисление разности чисел
    for i in range(1, len(numbers)):
        result_sub -= numbers[i]

    # Вычисление частного чисел
    for i in range(1, len(numbers)):
        # Проверка на деление на ноль
        if numbers[i] == 0:
            print("Деление на ноль невозможно!")
            break
        result_div /= numbers[i]

    # Получение операции от пользователя
    operation = input("Введите операцию (+, -, *, /) -> ")

    # Вывод результата операции
    if operation == '+':
        print("Сумма чисел ->", result_sum)
    elif operation == '-':
        print("Разность чисел ->", result_sub)
    elif operation == '*':
        print("Произведение чисел ->", result_mul)
    elif operation == '/':
        print("Деление чисел ->", result_div)

# Вызов функции main() только если скрипт запущен непосредственно, 
# а не импортирован как модуль
if __name__ == "__main__":
    main()
