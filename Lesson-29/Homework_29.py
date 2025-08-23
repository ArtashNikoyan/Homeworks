from abc import ABC, abstractmethod
import math

# 1. Գրել Animal ծնող class՝ eat() և sleep() մեթոդներով:
#    - Այս մեթոդներից յուրաքանչյուրը պետք է վերադարձնի համապատասխան հաղորդագրություն, երբ կանչ է արվում։
#    - eat()-ը պետք է վերադարձնի "Animal is eating..." հաղորդագրությունը
#    - sleep()-ը պետք է վերադարձնի "Animal is sleeping..." հաղորդագրությունը
#    Ծրագիրը պետք է ներառի նաև երկու ժառանգ class-ներ, որոնք ժառանգում են Animal class-ը՝ Bird և Fish:
#    Այս class-ները Animal class-ից պետք է ժառանգեն sleep() մեթոդը, բայց նաև պետք է ներառեն իրենց մեթոդները՝ ներկայացնելու համար կենդանիներին բնորոշ վարքագիծը:
#    - Bird class-ում, փոփոխեք eat() մեթոդը՝ "Bird is pecking at its food..." հաղորդագրությունը վերադարձնելու համար։
#    - Բացի այդ, ներառեք fly() մեթոդը, որը վերադարձնում է "Bird is flying..." հաղորդագրությունը:
#    - Fish class-ում ներառեք swim() մեթոդը, որը վերադարձնում է "Fish is swimming..." հաղորդագրությունը:


class Animal:
    def eat(self):
        print('Animal is eating...')
    
    def sleep(self):
        print('Animal is sleeping...')


class Bird(Animal):
    def eat(self):
        print('Bird is pecking at its food...')
    
    def fly(self):
        print('Bird is flying...')


class Fish(Animal):
    def swim(self):
        print('Fish is swimming...')


# f1 = Fish()
# f1.eat()
# f1.sleep()
# f1.swim()
#
# b1 = Bird()
# b1.eat()
# b1.sleep()
# b1.fly()

# 2․ Գրել Shape abstract class, որը․
#    - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
#    Գրել Circle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի շրջանագծի շառավիղը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։
#    Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։
#    Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի
#      -- կամ եռանկյան երեք կողմերը,
#      -- կամ մեկ կողմը և բարձրությունը,
#      -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
#    - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
#    - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
#      1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
#      2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
#      3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։


class ShapeAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def area(self):
        pass


class Circle(ShapeAbstract):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Radius must be a positive number')
        self.radius = radius
        
    def perimeter(self):
        return 2 * self.radius * math.pi
    
    def area(self):
        return math.pi * self.radius ** 2
    

class Rectangle(ShapeAbstract):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError('Width and height must be positive numbers')
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * self.width + self.height
    
    def area(self):
        return self.width * self.height
    
    
class Triangle(ShapeAbstract):
    
    def __init__(self, a, b=0, c=0, h=0, alpha=0):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.alpha = alpha
        
        if a and b and c:
            if a + b <= c or a + c <= b or b + c <= a:
                raise ValueError("Invalid triangle: sum of any two sides must be greater than the third.")
        elif a and h:
            if h <= 0:
                raise ValueError("Invalid triangle: height must be positive.")
        elif a and b and alpha:
            if alpha <= 0 or alpha >= 180:
                raise ValueError("Invalid triangle: angle must be between 0 and 180 degrees.")
        else:
            raise ValueError("Invalid triangle: not enough parameters.")
            
            
    def perimeter(self):
        if self.a and self.b and self.c:
            return self.a + self.b + self.c
        raise ValueError("Cannot calculate perimeter: all three sides are required.")
        
    def area(self):
        a, b, c, h, alpha = self.a, self.b, self.c, self.h, self.alpha
        
        if a and b and c:
            p = (a + b + c) / 2
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5
        elif a and h:
            return a * h / 2
        elif a and b and alpha:
            return a * b * math.sin(math.radians(alpha)) / 2
        
        return 0
        
