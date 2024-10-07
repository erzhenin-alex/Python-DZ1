#Ерженин Александр ДПИ23-1с
#Задание 2


class Vedomost:
    # Атрибут класса
    spisok_disciplin = ["Математика", "Физика", "Информатика", "История", "Литература"]

    def __init__(self, disciplina, gruppa):
        # Проверяем, что дисциплина входит в список дисциплин
        if disciplina not in Vedomost.spisok_disciplin:
            raise ValueError(f"Дисциплина {disciplina} не найдена в списке дисциплин.")
        
        self.disciplina = disciplina
        self.gruppa = gruppa
        self.vedomost = {}  # Словарь для хранения данных (фамилия: оценка)

    def put(self, familia, ocenka):
        # Проверка на допустимые оценки
        if ocenka not in ["отлично", "хорошо", "удовл.", "неудовл.", "н/я"]:
            raise ValueError("Недопустимая оценка!")
        self.vedomost[familia] = ocenka

    def get(self, familia):
        return self.vedomost.get(familia, "Студент не найден")

    def change(self, familia, novaya_ocenka):
        if familia in self.vedomost:
            if novaya_ocenka not in ["отлично", "хорошо", "удовл.", "неудовл.", "н/я"]:
                raise ValueError("Недопустимая новая оценка!")
            self.vedomost[familia] = novaya_ocenka
        else:
            print(f"Студент с фамилией {familia} не найден.")

    def delete(self, familia):
        if familia in self.vedomost:
            del self.vedomost[familia]
        else:
            print(f"Студент с фамилией {familia} не найден.")

    def result(self):
        # Подсчет количества каждого типа оценок
        otlichno = sum(1 for ocenka in self.vedomost.values() if ocenka == "отлично")
        khorosho = sum(1 for ocenka in self.vedomost.values() if ocenka == "хорошо")
        udovl = sum(1 for ocenka in self.vedomost.values() if ocenka == "удовл.")
        neudovl = sum(1 for ocenka in self.vedomost.values() if ocenka == "неудовл.")
        n_y = sum(1 for ocenka in self.vedomost.values() if ocenka == "н/я")
        return (otlichno, khorosho, udovl, neudovl, n_y)

    def __str__(self):
        header = f"Дисциплина: {self.disciplina}, Группа: {self.gruppa}\n"
        header += "--------------------------------------\n"
        header += "Фамилия      | Оценка\n"
        header += "--------------------------------------\n"
        body = "\n".join([f"{familia:12} | {ocenka}" for familia, ocenka in self.vedomost.items()])
        return header + body + "\n"

    def count(self):
        return len(self.vedomost)

    def names(self):
        return list(self.vedomost.keys())


# Пример использования класса
vedomost = Vedomost("Математика", "Группа 101")

# Добавление студентов и их оценок
vedomost.put("Иванов", "отлично")
vedomost.put("Петров", "хорошо")
vedomost.put("Сидоров", "удовл.")
vedomost.put("Кузнецов", "неудовл.")
vedomost.put("Смирнов", "н/я")

# Получение информации
print(vedomost)  # Печать всей ведомости
print("Оценка Петрова:", vedomost.get("Петров"))  # Оценка студента

# Изменение оценки
vedomost.change("Смирнов", "хорошо")
print("Измененная ведомость:\n", vedomost)

# Удаление студента
vedomost.delete("Сидоров")
print("После удаления Сидорова:\n", vedomost)

# Результаты подсчета
print("Статистика по оценкам:", vedomost.result())

# Количество студентов и их фамилии
print("Количество студентов:", vedomost.count())
print("Фамилии студентов:", vedomost.names())
