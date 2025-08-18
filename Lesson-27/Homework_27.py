import math

"""
1․ Գրել Triangle class, որը․
   - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
     եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
   - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
   - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
   - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
   - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն),
   - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը ուղղանկյուն եռանկյուն է, թե ոչ,
   - կունենա մեթոդ, որը կգտնի եռանկյան անկյունները,
   - կարող եք գրել նաև այլ մեթոդներ, որոնց միջոցով կստանաք տրված եռանկյան վերաբերյալ այլ ինֆորմացիա
     (օրինակ՝ ներգծած և արտագծած շրջանագծերի շառավղերը և այլն)․ բանաձևերը կարող եք գտնել համացանցում։
"""


class Triangle:
    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("A triangle with these sides does not exist!")
        
        self.a = a
        self.b = b
        self.c = c
        self._area = None
        self._type = None
        self._right = None
    
    def __str__(self):
        return f'Triangle sides: a - {self.a}, b - {self.b}, c - {self.c}'
    
    def is_right(self):
        sides = sorted([self.a, self.b, self.c])
        self._right = sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
        
        return self._right
    
    def type(self):
        if self.a == self.b == self.c:
            self._type = 'Equilateral'
        elif self.is_right():
            self._type = 'Right'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            self._type = 'Isosceles'
        else:
            self._type = 'Scalene'
        
        return self._type
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        t = self.type()
        if t == 'Equilateral':
            self._area = (self.a ** 2 * 3 ** 0.5) / 4
        elif t == 'Right':
            sides = sorted([self.a, self.b, self.c])
            self._area = sides[0] * sides[1] / 2
        else:
            p = self.perimeter() / 2
            self._area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        
        return round(self._area, 2)
    
    def get_angles(self):
        a, b, c = self.a, self.b, self.c
        alpha = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
        beta = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
        gamma = math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
        
        return round(alpha, 2), round(beta, 2), round(gamma, 2)
    
    def get_R(self):
        S = self.area()
        return round((self.a * self.b * self.c) / (4 * S), 2)
    
    def get_r(self):
        S = self.area()
        p = self.perimeter() / 2
        return round(S / p, 2)
    
    def get_heights(self):
        a, b, c = self.a, self.b, self.c
        S = self.area()
        return round(2 * S / b, 2), round(2 * S / a, 2), round(2 * S / c, 2)


# triangle1 = Triangle(2, 3, 6)  # invalid
triangle2 = Triangle(5, 5, 5)  # equilateral
triangle3 = Triangle(6, 6, 4)  # isosceles
triangle4 = Triangle(7, 8, 9)  # scalene
triangle5 = Triangle(3, 4, 5)  # right

# print(triangle1)
# print(triangle1.perimeter())
# print(triangle1.area())
# print(triangle1.type())
# print(triangle1.is_right())
# print(triangle1.get_angles())
# print(triangle1.get_R())
# print(triangle1.get_r())
# print(triangle1.get_heights())

print('-' * 100)

print(triangle2)
print(triangle2.perimeter())
print(triangle2.area())
print(triangle2.type())
print(triangle2.is_right())
print(triangle2.get_angles())
print(triangle2.get_R())
print(triangle2.get_r())
print(triangle2.get_heights())

print('-' * 100)

print(triangle3)
print(triangle3.perimeter())
print(triangle3.area())
print(triangle3.type())
print(triangle3.is_right())
print(triangle3.get_angles())
print(triangle3.get_R())
print(triangle3.get_r())
print(triangle3.get_heights())

print('-' * 100)

print(triangle4)
print(triangle4.perimeter())
print(triangle4.area())
print(triangle4.type())
print(triangle4.is_right())
print(triangle4.get_angles())
print(triangle4.get_R())
print(triangle4.get_r())
print(triangle4.get_heights())

print('-' * 100)

print(triangle5)
print(triangle5.perimeter())
print(triangle5.area())
print(triangle5.type())
print(triangle5.is_right())
print(triangle5.get_angles())
print(triangle5.get_R())
print(triangle5.get_r())
print(triangle5.get_heights())
