student_scores = input().split()
max_score = int(student_scores[0])
for score in student_scores:
    score = int(score)
    if score > max_score:
        max_score = score

print(f"The highest score in class is: {max_score}")