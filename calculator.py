def main():
    numbers = []

    print("Введите числа (для завершения введите 'stop') -> ")

    while True:
        input_num = input()
        if input_num == "stop":
            break

        if input_num == "":
            print("Введите число или 'stop' -> ")
            continue

        try:
            number = int(input_num)
            numbers.append(number)
        except:
            print("Некорректный ввод!")

    result_sum = sum(numbers)
    result_mul = 1
    result_sub = numbers[0]
    result_div = numbers[0]

    for num in numbers:
        result_mul *= num

    for i in range(1, len(numbers)):
        result_sub -= numbers[i]

    for i in range(1, len(numbers)):
        if numbers[i] == 0:
            print("Деление на ноль невозможно!")
            break
        result_div /= numbers[i]

    operation = input("Введите операцию (+, -, *, /) -> ")

    if operation == '+':
        print("Сумма чисел ->", result_sum)
    elif operation == '-':
        print("Разность чисел ->", result_sub)
    elif operation == '*':
        print("Произведение чисел ->", result_mul)
    elif operation == '/':
        print("Деление чисел ->", result_div)

if __name__ == "__main__":
    main()
