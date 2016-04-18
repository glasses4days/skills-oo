class Student(object):

    def __init__(self, first_name, last_name, address):
        """Initialize student attribute"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        """Initialize question and correct answer"""

        self.question = question
        self.correct_answer = correct_answer
        q_and_a = {}
        q_and_a[self.question] = self.correct_answer


class Exam(Question):

    def __init__(self, name):

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
       self.questions.append(super(Exam, self).__init__(question, correct_answer))
       #I'm trying add the question and answer using the Question object. It won't
       #append and I'm not sure why.