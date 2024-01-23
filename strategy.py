from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, first_operand, second_operand):
        pass


class Addition(Operation):
    def execute(self, first_operand, second_operand):
        return first_operand + second_operand


class Subtract(Operation):
    def execute(self, first_operand, second_operand):
        return first_operand - second_operand


class Multiply(Operation):
    def execute(self, first_operand, second_operand):
        return first_operand * second_operand


class Divide(Operation):
    def execute(self, first_operand, second_operand):
        if second_operand == 0:
            raise ZeroDivisionError
        else:
            return first_operand / second_operand


class Calculator:
    def __init__(self, first_operand, second_operand, operation=Addition()):
        self._first_operand = first_operand
        self._second_operand = second_operand
        self._operation = operation

    def __str__(self):
        return '' if str(self.calculate()) == "None" else str(self.calculate())

    def set_strategy(self):
        print("Choose your operation: \n"
              "\tAddition - 1\n"
              "\tSubtract - 2\n"
              "\tMultiply - 3\n"
              "\tDivide   - 4\n")
        user_choose = input()

        match user_choose:
            case '1':
                self._operation = Addition()
            case '2':
                self._operation = Subtract()
            case '3':
                self._operation = Multiply()
            case '4':
                self._operation = Divide()
            case _:
                print("Invalid input! Try again!")
                self.set_strategy()

    def calculate(self):
        try:
            return self._operation.execute(self._first_operand,
                                           self._second_operand)
        except ZeroDivisionError:
            print("Zero Division Error!")


if __name__ == "__main__":
    while True:
        is_work = input('Введите exit для выхода,'
                        ' иначе введите любое значение: ')
        if is_work == 'exit':
            # exit - для выхода из программы.
            # 0- показывает что код завершен без ошибок.
            # лучше всяких там break, но енто не точно.
            exit(0)

        first = input("Введите первое число: ")
        second = input("Введите второе число: ")
        try:
            first, second = float(first), float(second)
            calculator = Calculator(first, second)
            calculator.set_strategy()
            print(calculator)
        except ValueError:
            print("Вы ввели не числа!")
