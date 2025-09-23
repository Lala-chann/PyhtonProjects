student_scores = [8,65, 89, 86, 55, 91, 64, 89]

min_score = 0
for score in student_scores:
    if score > min_score:
        min_score = score
print(min_score)