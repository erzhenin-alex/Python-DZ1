#Ерженин Александр ДПИ23-1с
#Задание 3

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет."

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


# Класс Worker (наследуется от People)
class Worker(People):
    def __init__(self, name, age, post, salary):
        # Вызов конструктора базового класса People
        super().__init__(name, age)
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
        # Используем информацию из базового класса и добавляем данные о должности и зарплате
        return super().__str__() + f", Должность: {self.post}, Зарплата: {self.salary}"


# Создаем объект класса People
person = People("Анна", 25)
print(person)  # Вывод информации о человеке
print(person.introduce(),'\n')  

# Создаем объект класса Worker
worker = Worker("Иван", 30, "Программист", 150000)
print(worker)  # Вывод информации о сотруднике

# Получение информации о сотруднике через метод
print(worker.get_info(),'\n')

# Изменение зарплаты сотрудника
worker.set_salary(180000)
print(worker)  # Вывод обновленной информации о сотруднике
