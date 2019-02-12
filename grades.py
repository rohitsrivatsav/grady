# read in grades.txt
# print out a list of students
# and their avg grade for class
# and rank them in order
# from high to low
# i.e., bob 98, sue 97, sara 76


from collections import defaultdict


def average():
    students = {}
    students_count = {}
    with open("grades.txt") as f:
        for row in f:
            student, grade = row.strip().split(' ')
            if student not in students:
                students[student] = float(grade)
                students_count[student] = 1
            else:
                students[student] += float(grade)
                students_count[student] += 1

        for name in students:
            students[name] = round(students[name] / students_count[name], 2)
    return students


students = average()
for key, value in sorted(students.items(), key=lambda k: (k[1], k[0]), reverse=True):
    print(key, value)


# # Instructor code


# def get_grades(fn):
#     grades = defaultdict(list)
#     with open(fn) as f:
#         for line in f:
#             name, grade = line.strip().split(' ')
#             grade = float(grade)
#             grades[name].append(grade)
#         return grades


# def get_averages(grades):
#     averages = []
#     for name, scores in grades.items():
#         averages.append([name], sum(scores) / len(scores))
#     return averages


# def rank_scores(avgs):
#     return sorted(avgs, key=lambda t: t[1])[::-1]
