# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Cars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self._engine(name)
        self.TruePolice(is_police)

    def _engine(self, name):
        print(name, " завелась")

    def TruePolice(self,switch):
        if switch == True:
            print("Андрюха, у нас True, возможно криминал!")
            print("По коням!")
        else:
            print("it's not GTA")

class Control(Cars):

    def side(self, move):
        self.move = move
        if move == "l":
            print(" повернула налево")
        elif move == "r":
            print(" повернула направо")
        elif move == "s":
            print(" едет прямо")
        elif move == "d":
            print(" остановилась")

car_1 = Control(60,"green","TownCar",False)
car_2 = Control(120,"red","SportCar",False)
car_3 = Control(40,"grey","WorkCar",False)
car_4 = Control(80,"blue","PoliceCar",True)

car_1.side("d")
car_2.side("s")
car_3.side("l")
car_4.side("s")

