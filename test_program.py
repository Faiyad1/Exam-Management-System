'''
Execute this python file
'''
import question


def testing_short_questions():
    # Details for Short Questions:
    qtype = 'Short'
    correct_answer = 'Bob'
    marks = 1

    # responses also contain length of responses which are other than string
    responses = {
        'Positive': ['3Hi3', 'Bob'],
        'Negative': ['', (('A', 'B'), 10)],
        'Edge': ['Z', '1']
    }

    print_required_text(qtype, correct_answer, marks, responses)


def testing_single_questions():
    # Details for Single Questions:
    qtype = 'Single'
    correct_answer = 'B'
    marks = 1

    # responses also contain length of responses which are other than string
    responses = {
        'Positive': ['B', 'C'], 'Negative': [(4, 1), 'A, B'], 'Edge': ['A', 'D']
    }

    print_required_text(qtype, correct_answer, marks, responses)


def testing_multiple_questions():
    # Details for Multiple Questions:
    qtype = 'Multiple'
    correct_answer = 'A, B'
    marks = 2

    # responses also contain length of responses which are other than string
    responses = {
        'Positive': ['A, B', 'A'],
        'Negative': [(['A, B'], 8), 'E, F'],
        'Edge': ['A, B, E, :)', 'B, B, C, D']
    }

    print_required_text(qtype, correct_answer, marks, responses)


def print_required_text(qtype, correct_answer, marks, responses):
    first_time = True
    cases = ['Positive', 'Negative', 'Edge']
    i = 0
    while i < len(cases):
        j = 0
        while j < len(responses[cases[i]]):
            # Section 1: Assigning question object and marking response
            response = responses[cases[i]][j]
            question_object = question.Question(qtype)
            question_object.set_correct_answer(correct_answer)
            question_object.set_marks(marks)
            mark_attained = question_object.mark_response(response)

            # Section 2: Displaying the details of the question (for first time only)
            if first_time:
                print(f'\nQuestion type = {qtype}\n'
                      f'Correct answer = {correct_answer}   Marks = {marks}\n')
                first_time = False

            # Section 3: Displaying required text
            if isinstance(response, str) and cases[i] != 'Edge':
                length = 11 - len(response)
                print(f"Marks attained for {qtype} {cases[i]} case{j + 1},"
                      f" for input '{response}' {' ' * length} =", mark_attained)
            elif isinstance(response, str) and cases[i] == 'Edge':
                length = 11 - len(response)
                print(f"Marks attained for {qtype} {cases[i]} case{j + 1},    "
                      f" for input '{response}' {' ' * length} =", mark_attained)
            else:
                length = 13 - response[1]
                print(f"Marks attained for {qtype} {cases[i]} case{j + 1},"
                      f" for input {response[0]} {' ' * length} =", mark_attained)

            j += 1
        i += 1
    print()


# Running the functions
testing_short_questions()
testing_single_questions()
testing_multiple_questions()

