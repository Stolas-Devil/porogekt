class Critter:
    """фудболист"""
    total = 0

    def status():
        print("Общее число фудболистов", Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans

    def name(self):
        return self.__name

   
    def name(self, new_name):
        if new_name == "":
            print("Имя фудболиста не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)
main()

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)
main()

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)
main()

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)
main()

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)
main()

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)

def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)

main()  