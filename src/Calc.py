def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):
    return int(b) - int(a)


def multiplication(a, b):
    return int(a) * int(b)


def division(a, b):
    return int(b) / int(a)


def square(a):
    return int(a) * int(a)


def squareRoot(a):
    return int(a) ** (1 / 2)


class Calc:
    # Initialization
    result = 0


    def __init__(self):
        pass


    # Addition
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    # Subtraction
    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    # Multiplication
    def multiple(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    # Division
    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    # Square
    def sq(self, a):
        self.result = square(a)
        return self.result

    # SquareRoot
    def sqrt(self, a):
        self.result = squareRoot(a)
        return self.result
