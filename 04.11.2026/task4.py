students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

over_20 = filter(lambda student: student["age"] > 20, students)
print([student["name"] for student in over_20])

group_B = filter(lambda student: student["group"] == "B", students)
print([student["name"] for student in group_B])

avg_85 = filter(lambda student: sum(student["scores"]) / len(student["scores"]) >= 85, students)
print([student["name"] for student in avg_85])

group_A_avg_90 = filter(
    lambda student: student["group"] == "A" and sum(student["scores"]) / len(student["scores"]) >= 90,students,)
print([student["name"] for student in group_A_avg_90])