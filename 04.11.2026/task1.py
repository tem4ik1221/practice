students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

print(len(students))

list_names = [student["name"] for student in students]
print(list_names)

set_groups = {student["group"] for student in students}
print((set_groups))

list_tuples = [(student["name"], student["age"]) for student in students]
print(list_tuples)

dict_name_age = {student["name"]: student["age"] for student in students}
print(dict_name_age)

junior = min(students, key=lambda student: student["age"])
older = max(students, key=lambda student: student["age"])
print(junior["name"], junior["age"])
print(older["name"], older["age"])