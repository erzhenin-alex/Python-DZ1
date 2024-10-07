#Ерженин Александр ДПИ23-1с
#Задание 5

class Student:
    def __init__(self, name):
        self.name = name  # Имя студента (фамилия)
        self.disciplines = {}  # Словарь дисциплин, ключ - название дисциплины, значение - оценка

    # Метод для добавления дисциплины и оценки
    def put(self, discipline, grade):
        self.disciplines[discipline] = grade
        print(f"Дисциплина '{discipline}' с оценкой '{grade}' добавлена. ")

    # Метод для возврата списка сданных дисциплин (тех, у которых есть оценка)
    def sdan(self):
        return [discipline for discipline, grade in self.disciplines.items() if grade is not None]

    def __str__(self):
        disciplines_info = "\n".join([f"{discipline}: {grade}" for discipline, grade in self.disciplines.items()])
        return f"\n Студент: {self.name}\n Список дисциплин и оценок:\n{disciplines_info}"


# Создаем объект класса Студент
student = Student("Иванов")

# Добавляем дисциплины и оценки
student.put("Математика", "отлично")
student.put("Физика", "хорошо")
student.put("История", "удовл.")

# Печать информации о студенте
print(student ,'\n')

# Получение списка сданных дисциплин
sdan_disciplines = student.sdan()
print(f"Сданные дисциплины: {', '.join(sdan_disciplines)}")
