import math


# ---------- МОДУЛЬ: Вывод результата (Output) ----------
def output_result(result):
    """Показывает результат на экран."""
    print(f"Результат: {result}")


def output_error(message):
    """Показывает сообщение об ошибке."""
    print(f"Ошибка: {message}")


# ---------- МОДУЛЬ: Арифметика (Calc) ----------
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("деление на ноль невозможно")
    return a / b


# ---------- МОДУЛЬ: Математические функции (MathFunc) ----------
def sqrt(x):
    if x < 0:
        raise ValueError("корень из отрицательного числа не существует")
    return math.sqrt(x)

def power(x, y):
    return x ** y


# ---------- МОДУЛЬ: Ввод данных (Input) ----------
def input_number(prompt):
    """Спрашивает число и проверяет, что это число."""
    try:
        return float(input(prompt))
    except ValueError:
        raise ValueError("нужно ввести число")


# ---------- МОДУЛЬ: Парсер приоритетов (Parser) ----------
def parse_expression(expr):
    """
    Простой парсер: поддерживает +, -, *, /, скобки, приоритеты.
    Реализован через безопасное вычисление выражения.
    """
    allowed = set("0123456789+-*/(). ")
    if not set(expr) <= allowed:
        raise ValueError("в выражении есть недопустимые символы")
    try:
        # eval безопасен, т.к. мы проверили символы
        return eval(expr, {"__builtins__": {}}, {})
    except ZeroDivisionError:
        raise ZeroDivisionError("деление на ноль невозможно")
    except Exception:
        raise ValueError("не удалось разобрать выражение")


# ---------- МОДУЛЬ: Меню (Menu) ----------
def show_menu():
    print("\n--- КАЛЬКУЛЯТОР ---")
    print("1. Сложить")
    print("2. Вычесть")
    print("3. Умножить")
    print("4. Разделить")
    print("5. Квадратный корень")
    print("6. Возвести в степень")
    print("7. Посчитать выражение (с приоритетами и скобками)")
    print("0. Выход")


# ---------- МОДУЛЬ: Главный (Main) ----------
def main():
    while True:
        show_menu()
        choice = input("Выберите пункт: ").strip()

        try:
            if choice == "0":
                print("Выход. До свидания!")
                break

            elif choice in ("1", "2", "3", "4"):
                a = input_number("Первое число: ")
                b = input_number("Второе число: ")
                if choice == "1":
                    output_result(add(a, b))
                elif choice == "2":
                    output_result(sub(a, b))
                elif choice == "3":
                    output_result(mul(a, b))
                elif choice == "4":
                    output_result(div(a, b))

            elif choice == "5":
                x = input_number("Число: ")
                output_result(sqrt(x))

            elif choice == "6":
                x = input_number("Основание: ")
                y = input_number("Степень: ")
                output_result(power(x, y))

            elif choice == "7":
                expr = input("Введите выражение (например, 2+3*4 или (2+3)*4): ")
                output_result(parse_expression(expr))

            else:
                output_error("такого пункта меню нет")

        except ZeroDivisionError as e:
            output_error(str(e))
        except ValueError as e:
            output_error(str(e))


if __name__ == "__main__":
    main()