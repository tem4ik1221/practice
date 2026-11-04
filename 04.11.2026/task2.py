students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

names_A =[student["name"] for student in students if student["group"] == "A"]
print(names_A)

list_ages =([student["age"] for student in students])
print(list_ages)            

over_20 = [student["name"] for student in students if student["age"] > 20]
print(over_20)  

list_averages = [sum(student["scores"]) / len(student["scores"]) for student in students]
print(list_averages) 

list_descriptions = [f'{student["name"]} — {student["age"]} лет' for student in students]
print(list_descriptions)