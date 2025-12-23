import setup
import sys
import os
from exam import Exam


def parse_cmd_args(args):
    if len(args) < 3:
        print('Check command line arguments')

    elif not args[2].isdigit():
        print('Duration must be an integer')

    else:
        shuffle = False
        if len(args) > 3:
            if args[3] == '-r':
                shuffle = True
        return (args[1], int(args[2]), shuffle)


def setup_exam(obj):
    path1 = obj.path_to_dir + '/questions.txt'
    fobj = open(path1)
    question_objects = setup.extract_questions(fobj)

    obj.set_questions(question_objects)
    obj.set_exam_status()

    return (obj, obj.exam_status)


def main(args):
    exam_details = parse_cmd_args(args)
    if exam_details == None:
        return

    path1 = args[1] + '/questions.txt'
    path2 = args[1] + '/students.csv'
    if not os.path.isfile(path1) or not os.path.isfile(path2):
        print('Missing files')
        return

    print('Setting up exam...')
    try:
        obj = Exam(exam_details[1], exam_details[0], exam_details[2])
        obj, successful = setup_exam(obj)
        if successful:
            print('Exam is ready...')

            while True:
                preview = input('Do you want to preview the exam [Y|N]? ')
                if preview.lower() != 'y' and preview.lower() != 'n':
                    print("Invalid command.")
                elif preview.lower() == 'y':
                    print(obj.preview_exam(), end='')
                else:
                    return obj

        else:
            raise Exception
    except:
        print('Error setting up exam')


if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)

