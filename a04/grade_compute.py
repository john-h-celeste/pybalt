def grade_to_score(grade):
    grade = grade.upper()
    assert len(grade) > 0, 'Empty letter grade'
    assert len(grade) <= 2, 'Letter grade too long'
    assert grade[0] in 'ABCDF', 'Invalid letter grade'
    assert len(grade) < 2 or grade[1] in '+-', 'Invalid grade modifier'

    # mapping letter grade to score
    grade_table = {
        'A': 4,
        'B': 3,
        'C': 2,
        'D': 1,
        'F': 0,
    }

    # mapping modifier to score offset
    modifier_table = {
        '': 0, # no modifier - no change
        '-': -0.3,
        '+': 0.3,
    }

    score = grade_table[grade[0]]
    score += modifier_table[grade[1:]] # slice to handle grades without a modifier

    return score

def score_to_grade(score):
    # mapping score to letter grade
    grade_table = {
        4: 'A',
        3: 'B',
        2: 'C',
        1: 'D',
        0: 'F',
    }

    grade = grade_table[round(score)]

    diff = score - round(score) # difference between score and unmodified grade
    if diff > 0:
        grade += '+'
    elif diff < 0:
        grade += '-'

    return grade