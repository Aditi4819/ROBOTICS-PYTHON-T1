def numbers(students):
    num = {}
    for student in students:
        for course in student:
            if course not in num:
                num[course] = 0
            num[course] += 1
    return num

def popular(num):
    max_course, max_enroll = None, -1
    for course, enroll in num.items():
        if enroll > max_enroll:
            max_course, max_enroll = course, enroll
    return max_course


data = numbers([["math", "chem", "phy","cs"], ["math", "phy"], ["math", "chem"], ["history", "eco"]])

print(data)

print(popular(data))
