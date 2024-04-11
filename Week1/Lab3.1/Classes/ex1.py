class Uni: #проверяет, есть ли студент в списке
    def __init__(self, name):
        self.name = name

class Student(Uni):
    students = ["Linus", "Masha", "Batman", "Superman", "Ironman", "Spiderman", "Aquaman"]

    def getString(self):
        self.name = input("Enter the name of student: ")

    def printString(self):
        if self.name in self.students:
            print(f"Yes, {self.name} is student")

student1 = Student("Linus")
student2 = Student("Masha")
student3 = Student("Batman")
student4 = Student("Superman")
student5 = Student("Ironman")
student6 = Student("Spiderman")
student7 = Student("Aquaman")

student1.getString()
student1.printString()
