import setup
import sys
import program_two


def main(args):
    candidate_list = program_two.main(args)
    if candidate_list == None:
        return

    ask_for_sid = True
    sid_found = False
    first_time = True
    invalid_sid = 0
    invalid_input = 0
    invalid_name = 0

    while True:
        if ask_for_sid:
            sid = input('Enter your student identification number (SID) to start exam: ')

            # Section 1: Checking if sid is present (When sid is of right format)
            if isinstance(sid, str) and len(sid) == 9 and sid.isdigit():
                index = 0
                while index < len(candidate_list):
                    if candidate_list[index].sid == sid:
                        sid_found = True
                        break
                    index += 1

                # Displaying error message (When sid is not found in records)
                if not sid_found:
                    print('Candidate number not found for exam.')
                    ask_for_sid = False
                    invalid_input += 1

            # Displaying error message (When sid is of wrong format)
            else:
                print('Invalid SID.')
                invalid_sid += 1
                if invalid_sid == 3:
                    print('Contact exam administrator.')
                    return

        # Section 2: Verifying details (When sid is valid and found in records)
        if sid_found:
            while True:
                if first_time:
                    print('Verifying candidate details...')
                    first_time = False

                name = input('Enter your full name as given during registration of exam: ').lower()
                if candidate_list[index].set_confirm_details(sid, name):
                    print('Start exam....\n')
                    candidate_list[index].do_exam(False)
                    return

                # Displaying error message (When verification fails)
                else:
                    if invalid_name == 2:
                        print('Contact exam administrator to verify documents.')
                        return
                    print('Name does not match records.')
                    invalid_name += 1

        # Section 3: Asking if user wants to try again
        if not ask_for_sid:
            re_try = 0
            while True:
                inputted_text = input("Do you want to try again [Y|N]? ")
                re_try += 1
                if inputted_text.lower() == 'n':
                    return
                elif re_try == 4 or invalid_input == 3:
                    print('Contact exam administrator.')
                    return
                elif inputted_text.lower() == 'y':
                    ask_for_sid = True
                    break
                else:
                    print('Response must be [Y|N].')


if __name__ == "__main__":

    main(sys.argv)

