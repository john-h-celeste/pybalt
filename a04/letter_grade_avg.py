import grade_compute

def main():
    while (scores := process_input()) is not None:
        print('You entered the grades', ', '.join([grade_compute.score_to_grade(score) for score in scores]))
        lowest_score = min(scores)
        lowest_grade = grade_compute.score_to_grade(lowest_score)
        print(f'The lowest grade ({lowest_grade}) will be dropped.')
        scores.remove(lowest_score)
        avg_score = sum(scores) / len(scores)
        avg_grade = grade_compute.score_to_grade(avg_score)
        print(f'The resulting grade is {avg_grade} ({avg_score:.2}).')
    print('Bye!')

def process_input():
    grade1 = input('Enter the first grade or Q to quit: ')
    if grade1.upper() == 'Q':
        return None
    score1 = grade_compute.grade_to_score(grade1)
    grade2 = input('Enter the second grade: ')
    score2 = grade_compute.grade_to_score(grade2)
    grade3 = input('Enter the third grade: ')
    score3 = grade_compute.grade_to_score(grade3)
    grade4 = input('Enter the fourth grade: ')
    score4 = grade_compute.grade_to_score(grade4)
    return [score1, score2, score3, score4]

if __name__ == '__main__':
    main()