#Ерженин Александр ДПИ23-1с
#Задание 4


class Worker:
    def __init__(self, name, age, post, salary):
        self.name = name
        self.age = age
        self.post = post  # Должность
        self.salary = salary  # Зарплата

    # Метод для получения информации о сотруднике
    def get_info(self):
        return f"Должность: {self.post}, Зарплата: {self.salary}"

    # Метод для изменения зарплаты
    def set_salary(self, new_salary):
        self.salary = new_salary
        print(f"Зарплата для {self.name} изменена на {self.salary}.")

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Должность: {self.post}, Зарплата: {self.salary}"

# Класс Преподаватель (Teacher), который наследуется от класса Worker
class Teacher(Worker):
    def __init__(self, name, age, post, salary, disciplines=None):
        super().__init__(name, age, post, salary)  # Вызов конструктора родительского класса
        self.disciplines = disciplines if disciplines is not None else []  # Список дисциплин преподавателя

    # Метод для добавления дисциплины
    def add_dis(self, discipline):
        if discipline not in self.disciplines:
            self.disciplines.append(discipline)
            print(f"Дисциплина '{discipline}' добавлена.")
        else:
            print(f"Дисциплина '{discipline}' уже существует в списке.")

    # Метод для удаления дисциплины
    def delete_dis(self, discipline):
        if discipline in self.disciplines:
            self.disciplines.remove(discipline)
            print(f"Дисциплина '{discipline}' удалена.")
        else:
            print(f"Дисциплина '{discipline}' не найдена в списке.")

    # Переопределение метода __str__ для вывода информации о преподавателе
    def __str__(self):
        disciplines_str = ", ".join(self.disciplines) if self.disciplines else "нет дисциплин"
        return super().__str__() + f", Дисциплины: {disciplines_str}"


# Создаем объект преподавателя
teacher = Teacher("Мария Ивановна", 45, "Преподаватель", 60000, ["Математика", "Информатика"])

# Вывод информации о преподавателе
print(teacher ,'\n')

# Добавляем новую дисциплину
teacher.add_dis("Физика")
print(teacher,'\n')

# Пытаемся добавить уже существующую дисциплину
teacher.add_dis("Математика")
print(teacher,'\n')
# Удаляем дисциплину
teacher.delete_dis("Информатика")
print(teacher,'\n')

# Пытаемся удалить несуществующую дисциплину
teacher.delete_dis("История")
print(teacher,'\n')
# Проверка изменения зарплаты
teacher.set_salary(70000)
print(teacher)
