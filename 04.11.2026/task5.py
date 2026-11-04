students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

by_age = sorted(students, key=lambda student: student["age"])
print(by_age)

by_name = sorted(students, key=lambda student: student["name"])
print(by_name)

by_avg = sorted(students, key=lambda student: sum(student["scores"]) / len(student["scores"]), reverse=True)
print(by_avg)

by_group_age = sorted(students, key=lambda student: (student["group"], student["age"]))
print(by_group_age)

print("sort() vs sorted()")

sort_vs = students.copy()
sort_vs = list.sort(students, key=lambda student: student ["age"])
print("sort() сортирует на месте и возвращает None:", sort_vs)
print("Исходный список после sort():", students)
sorted_vs = sorted(students, key=lambda student: student ["age"])
print("sorted() возвращает новый список:", sorted_vs)