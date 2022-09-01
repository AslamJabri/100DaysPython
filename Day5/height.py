student_heights = input("Input the list of heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total = 0
for i in student_heights:
    total += i
print(total)
number_of_students = 0
for number_of_students in student_heights:
    number_of_students += 1
print(number_of_students)
average = total/number_of_students
print(average)