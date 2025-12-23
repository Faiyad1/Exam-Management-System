class Exam:
    def __init__(self, duration, path, shuffle):
        self.duration = duration
        self.path_to_dir = path
        self.shuffle = shuffle
        self.exam_status = False
        self.questions = []
        self.set_name(path)

    def set_name(self, path):
        self.name = path.split('/')[-1].replace(' ', '_')

    def get_name(self):
        return self.name.upper().replace('_', ' ')

    def set_exam_status(self):
        if self.questions != []:
            self.exam_status = True

    def set_duration(self, t):
        if t > 0:
            self.duration = t

    def set_questions(self, ls):
        if not isinstance(ls, list):
            return False

        i = 0
        while i < len(ls):
            if ls[i].description == None or ls[i].correct_answer == None:
                if ls[i].qtype != 'end':
                    print('Description or correct answer missing')
                    return False

            if len(ls[i].answer_options) != 4 and ls[i].qtype != 'end' \
                    and ls[i].qtype != 'short':
                print('Answer options incorrect quantity')
                return False

            if ls[i].answer_options != [] and ls[i].qtype == 'short':
                print('Answer options should not exist')
                return False

            if ls[i].qtype == 'end':
                if i != len(ls) - 1:
                    print('End marker missing or invalid')
                    return False
                if ls[i].answer_options != [] or ls[i].description != None \
                        or ls[i].correct_answer != None:
                    print('End marker missing or invalid')
                    return False

            if ls[i].qtype != 'end' and i == len(ls) - 1:
                print('End marker missing or invalid')
                return False

            i += 1

        self.questions = ls
        return True

    def preview_exam(self):
        preview = f'{self.get_name()}\n'
        i = 0
        length = len(self.questions)
        if length != 0:
            while i < length:
                preview += f"{self.questions[i].preview_question(i + 1)}\n\n"
                i += 1
        return preview

    def __str__(self):
        pass

    def copy_exam(self):
        new_exam = Exam(self.duration, self.path_to_dir, self.shuffle)

        new_questions = []
        i = 0
        while i < len(self.questions):
            original_question = self.questions[i]
            new_question = original_question.copy_question()
            new_questions.append(new_question)
            i += 1

        new_exam.questions = new_questions
        return new_exam

