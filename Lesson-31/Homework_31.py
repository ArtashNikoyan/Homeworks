# 1․ Գրել Calculator class, որը․
#    - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
#    - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
#    - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
#    - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__)։


class Calculator:
    @property
    def get_num(self):
        return self.__x
    
    def __init__(self, x):
        if isinstance(x, int | float):
            self.__x = x
        else:
            raise TypeError("Expected int or float")
    
    def __str__(self):
        return self.__x
    
    def __repr__(self):
        return f"{type(self.__x).__name__}: {self.__x}"
    
    # +
    def __add__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return Calculator(self.__x + other)
    
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        self.__x += other
        return self
    
    # -
    def __sub__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return Calculator(self.__x - other)
    
    def __rsub__(self, other):
        return Calculator(other - self.__x)
    
    def __isub__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        self.__x -= other
        return self
    
    # *
    def __mul__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return Calculator(self.__x * other)
    
    def __rmul__(self, other):
        self * other
    
    def __imul__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        self.__x *= other
        return self
    
    # /
    def __truediv__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return Calculator(self.__x / other)
    
    def __rtruediv__(self, other):
        return Calculator(other / self.__x)
    
    def __itruediv__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        self.__x /= other
        return self
    
    # //
    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return Calculator(self.__x // other)
    
    def __rfloordiv__(self, other):
        return Calculator(other // self.__x)
    
    def __ifloordiv__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        self.__x //= other
        return self
    
    # %
    def __mod__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return Calculator(self.__x % other)
    
    def __rmod__(self, other):
        return Calculator(other % self.__x)
    
    def __imod__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        self.__x %= other
        return self
    
    # **
    def __pow__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return Calculator(self.__x ** other)
    
    def __rpow__(self, other):
        self ** other
    
    def __ipow__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        self.__x **= other
        return self
    
    # ==
    def __eq__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return self.__x == other
    
    # !=
    def __ne__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return self.__x != other
    
    # <
    def __lt__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return self.__x < other
    
    # <=
    def __le__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return self.__x <= other
    
    # >
    def __gt__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return self.__x > other
    
    # >=
    def __ge__(self, other):
        if isinstance(other, Calculator):
            other = other.__x
        return self.__x >= other


# c1 = Calculator(10)
# c2 = Calculator(0)
#
# print(c1 / c2)


# EX 2
# Напишите класс Clock, который будет получать количество секунд в
# __init__ и будет иметь метод, возвращающий время в формате ЧЧ:ММ:СС.
# •Реализуйте магические методы операторов для увеличения
# количества секунд и сравнения их друг с другом
# (используйте все три типа оператора __add__).

class Clock:
    def __init__(self, seconds):
        self.seconds = seconds

    def __str__(self):
        sec = self.seconds % 60
        min = self.seconds // 60 % 60
        hour = self.seconds // 3600 % 24
        
        return f"{hour:02}:{min:02}:{sec:02}"

    def __add__(self, other):
        if isinstance(other, Clock):
            other = other.seconds
        return Clock(self.seconds + other)
    
    def __radd__(self, other):
            self + other
    
    def __iadd__(self, other):
        if isinstance(other, Clock):
            other = other.seconds
        self.seconds += other
        return self
    
    def __eq__(self, other):
        if isinstance(other, Clock):
            other = other.seconds
        return self.seconds == other
    
    def __ne__(self, other):
        if isinstance(other, Clock):
            other = other.seconds
        return self.seconds != other
    
    def __lt__(self, other):
        if isinstance(other, Clock):
            other = other.seconds
        return self.seconds < other
    
    def __le__(self, other):
        if isinstance(other, Clock):
            other = other.seconds
        return self.seconds <= other
    
    def __gt__(self, other):
        if isinstance(other, Clock):
            other = other.seconds
        return self.seconds > other
    
    def __ge__(self, other):
        if isinstance(other, Clock):
            other = other.seconds
        return self.seconds >= other

c = Clock(3600)
c1 = Clock(50000)

print(c)
print(c1)

c += c1
print(c)
print(c == c1)