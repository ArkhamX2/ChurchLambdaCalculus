class Person:

    def __init__(self, name, surname, skill=1):
        self.name = name
        self.surname = surname
        self.skill = skill

    def info(self):
        print("Здрайствуйте, меня зовут " + self.surname + " " + self.name + ". Я имею квалификацию уровня: " + str(self.skill))

    def faired(self):
        self.skill = 0
        print(self.surname + " " + self.name + " был уволен.")

    def up(self):
        self.skill = int(self.skill) + 1
        print(self.surname + " " + self.name + " был повышен.")

    def __del__ (self):
        print("До свидания, Мистер " + self.surname + " " + self.name)