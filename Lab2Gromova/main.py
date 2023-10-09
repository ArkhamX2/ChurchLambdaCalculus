import lib
from lib.person import Person


p1 = Person("Михаил", "Мяувин")
p1.info()
p2 = Person("Матвей", "Котиков", "2")
p2.info()
p3 = Person("Мурад", "Мурвин", "3")
p3.info()

p1.faired()
p2.up()
p2.info()
input()

