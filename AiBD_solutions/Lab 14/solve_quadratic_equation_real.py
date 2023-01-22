from typing import Union

class QuadraticEquationArgumentError(Exception): # Błąd pojawiający się w przypadku błędnych argumentów
    def __int__(self, message='Arguments must be int, or float type!'):
        self.message = message

# Funkcja zwraca None gdy nie ma rzeczywistych rozwiązań, float gdy jest jedno, lub dwuelementową krotkę gdy są dwa
def solve_quadratic_equation_real(a: Union[int, float], b: Union[int, float], c: Union[int, float], eps=10**(-14)) -> Union[float, tuple, None]:
    for arg in [a, b, c]:
        if not isinstance(arg, (int, float)):
            raise QuadraticEquationArgumentError()

    delta = b**2 - 4*a*c

    if -eps < delta < eps: # Uwzględnienie błędów numerycznych
        return -b/(2*a)
    elif delta < 0:
        return None
    else:
        sqd = delta**0.5
        return (-b - sqd)/(2*a), (-b + sqd)/(2*a)

