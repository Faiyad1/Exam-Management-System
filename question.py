class Question:
    def __init__(self, qtype):
        self.qtype = None
        self.set_type(qtype)
        self.description = None
        self.answer_options = []
        self.correct_answer = None
        self.marks = None

    def set_type(self, qtype):
        if qtype.lower() == 'single' or qtype.lower() == 'multiple' \
                or qtype.lower() == 'short' or qtype.lower() == 'end':
            self.qtype = qtype.lower()
            return True
        else:
            return False

    def set_description(self, desc):
        if self.qtype != 'end' and isinstance(desc, str) and len(desc) > 0:
            self.description = desc
            return True
        else:
            return False

    def set_correct_answer(self, ans):
        if self.qtype != 'end' and isinstance(ans, str) and len(ans) > 0:
            if self.qtype == 'single':
                if ans == 'A' or ans == 'B' or ans == 'C' or ans == 'D':
                    self.correct_answer = ans
                    return True
                else:
                    return False

            elif self.qtype == 'multiple':
                options = ans.split(',')
                i = count = 0
                while i < len(options):
                    opt = options[i].strip()
                    if opt == 'A' or opt == 'B' or opt == 'C' or opt == 'D':
                        count += 1
                    i += 1
                if count == len(options):
                    self.correct_answer = ans
                    return True
                else:
                    return False

            elif self.qtype == 'short':
                self.correct_answer = ans
                return True

            else:
                return False
        else:
            return False

    def set_marks(self, num):
        if self.qtype != 'end' and isinstance(num, int):
            if num >= 0:
                self.marks = num
                return True
            else:
                return False
        else:
            return False

    def set_answer_options(self, opts):
        if self.qtype == 'short' or self.qtype == 'end':
            self.answer_options = opts
            return True

        elif self.qtype == 'single' or self.qtype == 'multiple':

            # Section 1: Checking if variables opts and self.correct_answer is correctly labelled
            if len(opts) != 4:
                return False

            if not isinstance(opts, list):
                return False

            ans = self.correct_answer
            if not isinstance(ans, str):
                return False

            if not opts[0][0].startswith('A.') or not opts[1][0].startswith('B.') \
                    or not opts[2][0].startswith('C.') or not opts[3][0].startswith('D.'):
                return False

            if self.qtype == 'single':
                if ans != 'A' and ans != 'B' and ans != 'C' and ans != 'D':
                    return False

            if self.qtype == 'multiple':
                if len(ans) < 1:
                    return False

            i = 0
            while i < len(opts):
                if not isinstance(opts[i], tuple) or opts[i][1]:
                    return False
                i += 1

            # Section 2: Labelling variable opts
            optlist = []
            ans = self.correct_answer

            if self.qtype == 'single':
                i = 0
                while i < len(opts):
                    if opts[i][0].startswith(ans):
                        optlist.append((opts[i][0], True))
                    else:
                        optlist.append(opts[i])
                    i += 1

            elif self.qtype == 'multiple':
                options = ans.split(',')
                from setup import sort
                options = sort(options)
                i = j = 0
                while i < len(opts):
                    if j < len(options):
                        opt = options[j].strip()
                        if opts[i][0].startswith(opt):
                            optlist.append((opts[i][0], True))
                            j += 1
                        else:
                            optlist.append(opts[i])
                    else:
                        optlist.append(opts[i])
                    i += 1

            self.answer_options = optlist
            return True
        return False

    def get_answer_option_descriptions(self):
        if self.qtype == 'short' or self.qtype == 'end':
            return ''
        else:
            opts_list = self.answer_options
            preview_opts = ''
            i = 0
            while i < len(opts_list):
                preview_opts += f'{opts_list[i][0]}\n'
                i += 1
            return preview_opts.strip()

    def mark_response(self, response):
        ans = self.correct_answer
        mark = self.marks
        if not isinstance(response, str):
            return 0.0

        if self.qtype == 'multiple':
            options = ans.split(',')
            responses = response.split(',')
            from setup import sort
            options = sort(options)

            # Checking no. of correct inputted options
            i = correct = 0
            while i < len(options):
                j = 0
                while j < len(responses):
                    opt = options[i].strip()
                    responses_opt = responses[j].strip()

                    if opt == responses_opt:
                        correct += 1
                        break

                    j += 1
                i += 1

            if correct == 0:
                return 0.0
            else:
                final_mark = (correct / len(options)) * mark
                return round(final_mark, 2)

        else:
            if ans == response:
                return mark/1
            else:
                return 0.0

    def preview_question(self, i=0, show=True):
        if i == 0:
            i = 'X'
        if self.qtype == 'end':
            preview = '-End-'
            return preview

        else:
            if self.qtype == 'multiple':
                marks = f'Answers[{self.marks}]'
            else:
                marks = f'Answer[{self.marks}]'

            desc = ''
            if self.get_answer_option_descriptions() != '':
                desc = '\n' + self.get_answer_option_descriptions()

            if show:
                preview = f"""Question {i} - {self.qtype.title()} {marks}
{self.description}{desc}
Expected Answer: {self.correct_answer}"""
            else:
                preview = f"""Question {i} - {self.qtype.title()} {marks}
{self.description}{desc}"""

            return preview

    def generate_order():
        from random import randint
        list_no = []
        while len(list_no) < 4:
            no = randint(0, 3)

            if len(list_no) == 0:
                list_no.append(no)
            else:
                i = count = 0
                while i < len(list_no):
                    if no != list_no[i]:
                        count += 1
                    i += 1
                if count == len(list_no):
                    list_no.append(no)
        return list_no

    def shuffle_answers(self):
        if self.qtype == 'multiple' or self.qtype == 'single':
            random = Question.generate_order()
            opts = self.answer_options

            i = 0
            rearranged_opts = []
            while i < len(random):
                rearranged_opts.append(opts[random[i]])
                i += 1

            new_opts_list = []
            new_ans_list = []

            # Rearranging starting alphabet for options
            i = 0
            while i < len(rearranged_opts):
                opt_desc = rearranged_opts[i][0].partition('.')[-1]
                opt_no = ''

                if i == 0:
                    opt_no = 'A'
                elif i == 1:
                    opt_no = 'B'
                elif i == 2:
                    opt_no = 'C'
                elif i == 3:
                    opt_no = 'D'

                opt = opt_no + '.' + opt_desc
                new_opts_list.append((opt, rearranged_opts[i][1]))

                if rearranged_opts[i][1]:
                    new_ans_list.append(opt_no)

                i += 1
            self.answer_options = new_opts_list

            # Setting variable correct_answer
            new_ans = new_ans_list[0]
            i = 1
            while i < len(new_ans_list):
                new_ans += ', ' + new_ans_list[i]
                i += 1
            self.correct_answer = new_ans
        return None

    def __str__(self):
        '''
        You are free to change this, this is here for your convenience.
        When you print a question, it'll print this string.
        '''


        #return f'''Question {self.__hash__()}:

    def copy_question(self):
        new_question = Question(self.qtype)
        new_question.description = self.description
        new_question.answer_options = self.answer_options
        new_question.correct_answer = self.correct_answer
        new_question.marks = self.marks

        new_question.shuffle_answers()

        return new_question

