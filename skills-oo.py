class Student(object):

    def __init__(first_name, last_name, address):
        """Initialize student attribute"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(question, correct_answer):
        """Initialize question and correct answer"""

        self.question = question
        self.correct_answer = correct_answer

class Exam(Question):

    def __init__(name):

        self.name = name
        self.questions = []
