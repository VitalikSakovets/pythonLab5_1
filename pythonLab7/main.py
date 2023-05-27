# Реалізувати клас Vector3D з відповідними атрибутами
# (координатами вектора у просторі x, y, z) та
# перевантаженими операторами та арифметичними операціями
# (__str_(), __add__(), __iadd__(), __mul__(), __imul__(),
#  __neg__(), __sub__(), __isub__(), __abs__(), __truediv__(),
#  __eq__(), __ne__(),  __lt__(), __gt__() та інші ).
# Та продемонструвати роботу із вказаним класом.
import math

class Vector3D:
    def __init__(self,x=0,y=0,z=0): #*coord n-вимірного простору
        self.__x=x
        self.__y=y
        self.__z=z
        self.__vect=[self.__x,self.__y,self.__z]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self,x):
        self.__x=x

    @y.setter
    def y(self, y):
        self.__y = y

    @z.setter
    def z(self, z):
        self.__z = z

    def __repr__(self):
        return "("+str(self.__x)+", "+str(self.__y)+", "+str(self.__z)+")"

    def __str__(self):
        return "("+str(self.__x)+", "+str(self.__y)+", "+str(self.__z)+")"

    def __add__(self, vector):# Vector3D(3,4,6)+Vector3D(3,7,8) =?
        if isinstance(vector,Vector3D):
            v=Vector3D()
            v.x=self.x+vector.x
            v.y = self.y + vector.y
            v.z = self.z + vector.z
            return v
        if isinstance(vector,(int,float)):
            v = Vector3D()
            v.x = self.x + vector
            v.y = self.y + vector
            v.z = self.z + vector
            return v
        else:
            raise TypeError('Така операція не можлива')
    #vector1+=vector2, щоб зеберегти результат за тим самим self,
    # то краще в перевизначенні +=, *= і т.д. не икористовувати перевантажені
    # бінарні оператори. Адже в межах нашого класу у визначенні бінарного + створюється
    # і повертається новий обєкт
    def __iadd__(self, vector):
        if isinstance(vector,Vector3D):
            self.x=  self.x+vector.x
            self.y = self.y + vector.y
            self.z = self.z + vector.z
            return self
        if isinstance(vector,(int,float)):
            self.x = self.x + vector
            self.y = self.y + vector
            self.z = self.z + vector
            return self
        else:
            raise TypeError('Така операція не можлива')
        return self

    def __radd__(self, vector):
        # v = Vector3D()
        # v.x = vector.x+self.x
        # v.y = vector.y+ self.y
        # v.z = vector.z+ self.z
        # return v
        return self+vector

    def __mul__(self, vector):  # Vector3D(3,4,6)*Vector3D(3,7,8) =?
        if isinstance(vector, Vector3D):
            v = Vector3D()
            v.x = self.x * vector.x
            v.y = self.y * vector.y
            v.z = self.z * vector.z
            return v
        if isinstance(vector, (int, float)):
            v = Vector3D()
            v.x = self.x * vector
            v.y = self.y * vector
            v.z = self.z * vector
            return v
        else:
            raise TypeError('Така операція не можлива. Не відповідність типів! ')

    # def __sub__(self, other):
    # def __mul__(self, other):
    #скалярне множення векторів
    def scalyar(self, vector):
         return self.x * vector.x+self.y * vector.y+self.z * vector.z

    # def __truediv__(self, other):
    #__neg__(self)
    def __neg__(self):
        self.x=-self.x
        self.y=self.y*(-1)
        self.z=-self.z
        return self

    def __abs__(self):
        return   round(math.sqrt(self.x**2+self.y**2+self.z**2),2)

    def __eq__(self, vector):#self==vector
        if (self.x==vector.x and self.y==vector.y and self.z==vector.z):
            return True
        else:
            return False
    #>,<,!=,>=,<=
    def __gt__(self, vector):
        if abs(self)>abs(vector):
            return True
        else:
            return False

    def __len__(self):
        return len(self.__vect)

    def __getitem__(self, index):
        return self.__vect[index]

    def __setitem__(self, index, value):
        if index==0:
            self.x=value
            self.__vect[index]=value
        if index == 1:
            self.y=value
            self.__vect[index] = value
        if index == 2:
            self.z=value
            self.__vect[index] = value
        else:
            raise IndexError("Вихід за межі діапазону вектора! Нема елемента за таким індексом")


a=Vector3D(2,5,8)
b=Vector3D(1,7,1)
print(a)
print(b.x)
b.x=4
print(b)
print(a+b)
print(b+a)
a+=a
print(a)
a=a+2
print(a)
print(2+a)
print(a*2)
c=-a
print(c)
print('*'*35)
print("modul vectora a=",abs(a))#f'modul vectora a={round(abs(a))}'
print("modul vectora b=",abs(b))
print('*'*35)
a1=Vector3D(2,3,4)
a2=Vector3D(2,3,4)
print(a1==a2)
print(id(a1))
print(id(a2))
a3=a1
print(a1==a3)
print('*'*35)
a3=Vector3D(2,6,4)
a4=Vector3D(2,3,4)
print(a3>a4)
print(a4>a3)
print(len(a3))
print(a4[2])
a4[2]=9
print(a4)
# a4[3]=9