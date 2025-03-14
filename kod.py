import math
import numpy as np
import matplotlib.pyplot as plt



class Equation:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


    def discriminant(self):
        self.disc = ((self.b)**2 - 4 * (self.a)*(self.c))
        if self.disc > 0:
            self.x1 = (-(self.b) + math.sqrt(self.disc  )) / (2 * (self.a))
            self.x2 = (-(self.b) - math.sqrt(self.disc)) / (2 * (self.a))
            print(f'Первый корень уравнения{self.x1}')
            print(f'Второй корень уравнения{self.x2}')
    
        elif self.disc == 0:
            self.x = (-(self.b) / (2 * (self.a)))
            print(f'Единственный корень уравнения{self.x}')
        elif self.disc < 0:
            print('Ошибка')



    def graf(self):
        self.x = np.linspace(-10, 10, 50)
        self.y = self.a*self.x**2 + self.b*self.x + self.c  

        fig,self.ax = plt.subplots()

        self.ax.plot(self.x, self.y, color='red')   
        self.ax.set_title('График функции y') 
        self.ax.set_xlabel('Ось x') 
        self.ax.set_ylabel('Ось y') 
        self.ax.grid() 

        self.ax.set_xlim(-10, 10)  
        self.ax.set_ylim(-10, 10) 
        
    def show(self):   
        self.graf()
        plt.show()  


    def __del__(self):
        print('Класс удален')


class Line(Equation):

    def __init__(self,a ,b, c, d):
        super().__init__(a, b, c, d)

    def graf(self):
        super().graf()
        self.x = np.linspace(-10, 10, 2)
        self.y = self.a*self.x + self.b

        self.ax.plot(self.x, self.y, color ='green')  


    def __del__(self):
        print('Прямая удалена')

class Integral(Equation):

    def __init__(self,a ,b, c, d):
        super().__init__(a, b, c, d)

    def graf(self):
        super().graf()
        self.x = np.linspace(-10, 10, 100)
        self.y = self.a*self.x**3 + self.b*self.x**2 + self.c*self.x + self.d

        self.ax.plot(self.x, self.y, color='green') #создаем пометку 

    def __del__(self):
        print('Кубическое уравнение удалено')






first = Integral(1,5,2,3)
first.show()
second = Line(1,5,2,3)
second.show()




