student_heights = input().split()

total = 0
num_of_students = 0

for height in student_heights:
    height = int(height)
    total += height
    num_of_students += 1

print(f"Total height = {total}")
print(f"Total no of students = {num_of_students}")

avg_height = round(total/num_of_students)

print(avg_height)