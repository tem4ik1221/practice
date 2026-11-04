students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

names_upper = list(map(lambda student: student["name"].upper(), students))
print(names_upper)

age_plus_one = list(map(lambda student: student["age"] + 1, students))
print(age_plus_one)

averages = list(map(lambda student: sum(student["scores"]) / len(student["scores"]), students))
print(averages)

result = list(map(lambda student: {"name": student["name"], "average": sum(student["scores"]) / len(student["scores"])}, students))
print(result)