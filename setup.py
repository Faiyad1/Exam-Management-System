import question
import candidate
import io


def extract_questions(fobj: io.TextIOWrapper) -> list:
    contents = fobj.read()
    questions_list = contents.split('\n\n')
    obj_list = []

    if questions_list[-1] != 'end':
        questions_list.append('end')

    # Working with one question at a time
    i = 0
    while True:
        line = questions_list[i].strip().split('\n')

        # Section 1: Setting qtype   (if end is encountered then returning object list )
        if line[0].startswith('Question -'):
            qtype = line[0].split('-')[-1].strip()
            obj = question.Question(qtype)
            obj_list.append(obj)
            if obj.qtype == None:
                continue

        else:
            obj = question.Question('end')
            obj_list.append(obj)
            return obj_list

        #  Section 2: Setting correct_answer
        if line[-2].startswith('Expected Answer:'):
            correct_answer = line[-2].partition(':')[-1]
            obj_list[i].set_correct_answer(correct_answer.strip())

        #  Section 3: Setting marks
        if line[-1].startswith('Marks:'):
            marks = line[-1].partition(':')[-1]
            obj_list[i].set_marks(int(marks))

        j = 0
        desc_not_set = True
        while j < len(line) - 2:

            #  Section 4: Setting description
            if line[j + 1].startswith('A.') or line[j + 1].startswith('Possible Answers:') \
                    or line[j + 1].startswith('Expected Answer:'):

                if desc_not_set:
                    list_lines = line[1: j + 1]
                    description = ''
                    k = 0
                    while k < len(list_lines):
                        description += list_lines[k] + '\n'
                        k += 1
                    obj_list[i].set_description(description.strip())
                    desc_not_set = False

            #  Section 5: Setting answer_options
            if line[j].startswith('A.') or line[j - 1].startswith('Possible Answers:'):
                list_lines = []
                while j < len(line)-2:
                    list_lines.append((line[j], False))
                    j += 1
                obj_list[i].set_answer_options(list_lines)

            j += 1
        i += 1


def sort(to_sort: list, order: int = 0) -> list:
    if not isinstance(to_sort, list):
        return []

    if len(to_sort) == 0:
        return to_sort

    if order == 1:
        # Sorting when it has nested list or tuple (in ascending order)
        if isinstance(to_sort[0], tuple) or isinstance(to_sort[0], list):
            i = 0
            while i < len(to_sort):
                j = 0
                while j < len(to_sort)-1:
                    if to_sort[j][0] > to_sort[j+1][0]:
                        to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
                    j += 1
                i += 1

        # Sorting when it does not have nested list or tuple (in ascending order)
        else:
            i = 0
            while i < len(to_sort):
                j = 0
                while j < len(to_sort)-1:
                    if to_sort[j] > to_sort[j+1]:
                        to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
                    j += 1
                i += 1

    elif order == 2:
        # Sorting when it has nested list or tuple (in descending order)
        if isinstance(to_sort[0], tuple) or isinstance(to_sort[0], list):
            i = 0
            while i < len(to_sort):
                j = 0
                while j < len(to_sort)-1:
                    if to_sort[j][0] < to_sort[j+1][0]:
                        to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
                    j += 1
                i += 1

        # Sorting when it does not have nested list or tuple (in descending order)
        else:
            i = 0
            while i < len(to_sort):
                j = 0
                while j < len(to_sort)-1:
                    if to_sort[j] < to_sort[j+1]:
                        to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
                    j += 1
                i += 1

    return to_sort


def extract_students(fobj: io.TextIOWrapper) -> list:
    try:
        contents = fobj.read().strip()
    except:
        return []

    unsorted_records = contents.split('\n')[1:]
    list_of_records = sort(unsorted_records, 1)
    obj_list = []

    i = 0
    while i < len(list_of_records):
        record = list_of_records[i].strip(',').split(',')
        if len(record) == 2:
            candidate_obj = candidate.Candidate(record[0], record[1], 0)
        else:
            candidate_obj = candidate.Candidate(record[0], record[1], int(record[2]))
        obj_list.append(candidate_obj)
        i += 1

    return obj_list

