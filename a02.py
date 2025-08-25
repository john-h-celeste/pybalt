# manage student grades
# robert vail, 8/25/2025 AD

print('Welcome to the Grade Manager 2333 (tm).')

grades = {}

while True:
    choice = input('(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ')
    choice = choice.upper()

    if choice == 'A':
        name = input('Enter the student\'s name: ')
        if name in grades:
            print('That student already exists and cannot be added again.')
            continue
        
        gradestr = input('Enter the student\'s grade: ')
        try:
            grade = int(gradestr)
        except ValueError:
            print('Invalid grade entered.')
            continue
        
        grades[name] = grade
    elif choice == 'R':
        name = input('Enter the student\'s name: ')
        if name not in grades:
            print('That student does not exist and cannot be removed.')
            continue
        
        grades.pop(name)
    elif choice == 'M':
        name = input('Enter the student\'s name: ')
        if name not in grades:
            print('That student does not exist and cannot be modified.')
            continue
        print('The current grade is', grades[name])
        
        gradestr = input('Enter the student\'s new grade: ')
        try:
            grade = int(gradestr)
        except ValueError:
            print('Invalid grade entered.')
            continue
        
        grades[name] = grade
    elif choice == 'P':
        avg = sum(grades.values()) / len(grades)
        print('The average grade is', avg)
        print('Student grades:')
        for name,grade in grades.items():
            print(f'  {name}: {grade}')
    elif choice == 'Q':
        print('Thank you for using Grade Manager 2333 (r).')
        print('Goodbye!')
        break
    else:
        print('Invalid choice.')
