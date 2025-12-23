import setup
import program_one
import sys
import os


def assign_exam(exam):
    # Section 1: Extracting student records
    path2 = exam.path_to_dir + '/students.csv'
    if not os.path.isfile(path2):
        print('No candidates found in the file')
        return

    fobj = open(path2)
    candidate_list = setup.extract_students(fobj)
    if candidate_list == []:
        print('No candidates found in the file')
        return

    # Section 2: Assigning students exam object depending on shuffle
    print('Assigning exam to candidates...')
    i = 0
    obj_no = len(candidate_list)
    while i < obj_no:
        candidate_list[i].exam = exam
        if candidate_list[i].exam.shuffle:
            candidate_list[i].exam = candidate_list[i].exam.copy_exam()
        i += 1

    print(f'Complete. Exam allocated to {obj_no} candidates.')
    return candidate_list


def main(args):
    try:
        exam_obj = program_one.main(args)
        if exam_obj == None:
            return
        candidate_list = assign_exam(exam_obj)

        while True:
            sid = input("Enter SID to preview student's exam (-q to quit): ")
            if sid == '-q':
                return candidate_list
            elif sid == '-a':
                i = 0
                while i < len(candidate_list):
                    print(candidate_list[i].do_exam())
                    i += 1

            elif isinstance(sid, str) and len(sid) == 9 and sid.isdigit():
                i = 0
                while i < len(candidate_list):
                    if candidate_list[i].sid == sid:
                        print(candidate_list[i].do_exam())
                        break
                    i += 1
                if i == len(candidate_list):
                    print('SID not found in list of candidates.\n')

            else:
                print('SID is invalid.\n')
    except:
        pass


if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)

