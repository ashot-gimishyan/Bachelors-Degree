class Student:
    def __init__(self):
        self.name = "Иван"
        self.surname = "Смирнов"
        self.group = 100
        self.progress = [10,10,10,10,10]

    def __init__(self, name, surname, group, progress):
        self.name = name
        self.surname = surname
        self.group = group
        self.progress = progress
    def  display(self):
        print(f"Имя: {self.name}\nФамилия: {self.surname}\nГруппа: {self.group}\nУспеваемость: {self.progress}\n")

students = list()

for i in range(2):
    st = Student(input(), input(), int(input()), input().split())
    st.progress = [int(mark) for mark in st.progress]
    #st.display()
    students.append(st)


students = sorted(students, key=lambda st: sum(st.progress)/5 )

for student in students:
    student.display()
    print()


