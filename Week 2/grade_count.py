sum_grade = 0

for grade in range(5):
    grade = int(input())
    if 0 <= grade <= 100:
        sum_grade += grade
    else:
        print('None')

sum_grade /= 5

if sum_grade >= 90:
    letter_grade = 'A'
elif sum_grade >= 80:
    letter_grade = 'B'
elif sum_grade >= 75:
    letter_grade = 'C'
elif sum_grade >= 65:
    letter_grade = 'D'
elif sum_grade >= 60:
    letter_grade = 'E'
else:
    letter_grade = 'F'
    
print(f'Average grade = {sum_grade:.1f} -> {letter_grade}')

