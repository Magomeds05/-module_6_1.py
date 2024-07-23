class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Mammal(Animal):
    def eat(self,food):
        self.food = food
        print(self.name, 'съел', food.name)

class Predator(Mammal):
    def eat(self,food):
        self.food = food
        print(self.name, 'не стал есть', food.name)



class Plant:
    def __init__(self,name):
        self.edible = False
        self.name = name


class Flower(Plant):
    def eat(self,food):
        self.food = food

class Fruit(Flower):
    def eat(self,food):
        self.food = food



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)












