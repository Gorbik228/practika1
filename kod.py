import math
import matplotlib.patches
import matplotlib.pyplot as plt



class Equation:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


    def discriminant(self):
        d = ((self.b)**2 - 4 * (self.a)*(self.c))
        if d > 0:
            self.x1 = (-(self.b) + math.sqrt(d)) / (2 * (self.a))
            self.x2 = (-(self.b) - math.sqrt(d)) / (2 * (self.a))
            print(f'Первый корень уравнения{self.x1}')
            print(f'Второй корень уравнения{self.x2}')
    
        elif d == 0:
            self.x = (-(self.b) / (2 * (self.a)))
            print(f'Единственный корень уравнения{self.x}')
        elif d < 0:
            print('Ошибка')


    def __del__(self):
        print('Класс удален')

reshenie = Equation(1,10,1)
reshenie.discriminant()





