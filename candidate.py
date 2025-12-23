class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        return self.exam.duration + self.extra_time

    def edit_sid(self, sid):
        if isinstance(sid, str) and len(sid) == 9 and sid.isdigit():
            self.sid = sid

    def edit_extra_time(self, t):
        if isinstance(t, int):
            if t >= 0:
                self.extra_time = t

    def set_confirm_details(self, sid, name):
        if sid == self.sid and name.lower() == self.name.lower():
            self.confirm_details = True
            return True
        else:
            return False

    def log_attempt(self, data):
        import os
        path = self.exam.path_to_dir + '/submissions'
        if os.path.isdir(path):
            path2 = self.exam.path_to_dir + '/submissions/' + self.sid + '.txt'
        else:
            os.makedirs(path)
            path2 = self.exam.path_to_dir + '/submissions/' + self.sid + '.txt'
        fobj = open(path2, 'w+')
        fobj.write(data)
        fobj.close()

    def set_results(self, ls):
        if self.confirm_details and len(ls) == len(self.exam.questions) - 1:
            self.results = ls

    def do_exam(self, preview=True):
        exam_preview = f"""Candidate: {self.name}({self.sid})
Exam duration: {self.get_duration()} minutes
You have {self.get_duration()} minutes to complete the exam.\n"""
        print(exam_preview, end='')

        if self.exam == None:
            line = f"Exam preview: \nNone\n"
            print(line)
            self.log_attempt(line)

        else:
            lines = self.exam.preview_exam().strip().split('\n')
            i = j = 0
            stored_lines = ''
            while i < len(lines):

                # Displaying response statement instead of correct_answer
                if lines[i].startswith('Expected Answer:'):
                    if not preview:
                        print(f'Response for Question {j + 1}: ', end='')
                        input_text = input()
                        line_one = f'Response for Question {j + 1}: ' + input_text
                        marks = self.exam.questions[j].mark_response(input_text)
                        line_two = f'You have scored {marks:.2f} marks.\n'
                        stored_lines += line_one + '\n' + line_two
                    else:
                        line_one = f'Response for Question {j + 1}: ' + '\n'
                        print(line_one, end='')
                        stored_lines += line_one
                    j += 1

                else:
                    line_one = lines[i] + '\n'
                    if i != 0:
                        stored_lines += line_one
                    print(line_one, end='')
                i += 1

            self.log_attempt(stored_lines.strip())
            return ''

    def __str__(self):
        '''
        You are free to change this, this is here for your debugging convenience.
        '''
        name = f"Candidate: {self.name}({self.sid})\n"
        t = self.get_duration()
        duration = f"Exam duration: {t} minutes\n"
        duration += "You have " + str(t) + " minutes to complete the exam.\n"
        if self.exam == None:
            exam = f"Exam preview: \nNone\n"
        else:
            exam = self.exam.preview_exam()
        str_out = name + duration + exam
        return str_out

