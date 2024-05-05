class Hero():
    def __init__(self, name, damage):
        self.name = name
        self.atack = damage
    
    def hello(self):
        print(self.name + ' говорит вам привет')


    def atack1(self):
        print(self.name + ' Бьет по всем врагам на ' + str(self.atack))

dima = Hero('Дима', 20)
tagir = Hero('Тагир', 25)

tagir.hello()
dima.hello()

tagir.atack1()
