# 1. Import a Python program with numpy package.
import numpy

# 2. Initialize a numpy array named grade_book with size (10, 5) with randomly generated number between [50,100]. Each row represents a student, and each column represents a subject. Each element in the array represents a student who has secured the grade on that respective subject.
grade_book = numpy.random.randint(50, 100, (10, 5))

print('Student grades:')
print(grade_book)

# 3. Compute average marks per student and per subject.
print()
print('Average grade by subject:')
print(grade_book.mean(0))
print('Average grade by student:')
print(grade_book.mean(1))

# 4. Find the highest and lowest marks in the entire array and identify which student and subject achieved them.
print()
print('Highest grade: ', end = '')
print(grade_book.max())
maxstudent,maxsubject = numpy.unravel_index(grade_book.argmax(), grade_book.shape)
print(f'Achieved by student {maxstudent + 1} in subject {maxsubject + 1}')

print()
print('Lowest grade: ', end = '')
print(grade_book.min())
minstudent,minsubject = numpy.unravel_index(grade_book.argmin(), grade_book.shape)
print(f'Achieved by student {minstudent + 1} in subject {minsubject + 1}')

# 5. Compute the overall class average.
print()
print('Average grade:')
print(grade_book.mean())

# 6. Create a view of all rows (students) whose total marks exceed the class average.
print()
print('Students with a higher than average grade:')
print(grade_book[grade_book.mean(1) > grade_book.mean()])
