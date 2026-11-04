students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]
 
def average(student):
    return sum(student["scores"]) / len(student["scores"])
 
filter_students = filter(lambda x: average(x) >= 80, students)
 
map_students = list(map(lambda x: {"name": x["name"], "group": x["group"], "average": average(x)}, students))
 
sorted_students = sorted(map_students, key=lambda x: x["average"], reverse=True)
 
for student in sorted_students[:3]:
    print(student["name"], student["average"])