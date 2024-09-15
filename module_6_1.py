# Домашнее задание по теме "Зачем нужно наследование"
# создание родительского класса Animal
class Animal:
    # атрибуты класса
    alive = True # живой
    fed = False # накормленный

    # создание объекта класса Animal
    def __init__(self, name):
        self.name = name # название животного

    # метод eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
    # Метод общий для дочерних классов Mammal и Predator, вынесен в родительский класс
    def eat(self, food):
        # условие проверки на съедобность Flowers или Fruit из класса Plant
        if food.edible == True:
            # наследованный атрибут fed объекта меняем на True. Первый вариант обращения к атрибуту класса
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            # наследованный атрибут alive объекта меняем на False. Второй вариант обращения к атрибуту класса
            Animal.alive = False
            print(f'{self.name} не стал есть {food.name}')
# создание родительского класса Plant
class Plant:
    edible = False # атрибут класса "съедобность"
    # инициализация объектов класса Plant
    def __init__(self, name):
        self.name = name # название растения

# создание дочернего класса Mammal класса Animal
class Mammal(Animal):
    # метод eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
    # def eat(self, food):
    #     if food.edible == True:
    #         self.fed = True
    #         print(f'{self.name} съел {food.name}')
    #     else:
    #         self.alive = False
    #         print(f'{self.name} не стал есть {food.name}')
    pass
# создание дочернего класса Predator класса Animal
class Predator(Animal):
    # метод eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
    # def eat(self, food):
    #     if food.edible == True:
    #         Animal.fed = True
    #         print(f'{self.name} съел {food.name}')
    #     else:
    #         Animal.alive = False
    #         print(f'{self.name} не стал есть {food.name}')
    pass
# создание дочернего класса Flower класса Plant
class Flower(Plant):
    # атрибут не присваивается, наследуется от родительского класса
    pass
# создание дочернего класса Fruit класса Plant
class Fruit(Plant):
    # объявление атрибута edible дочернего класа Fruit
    edible = True

# Исходные данные
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# вывод на консоль
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
