import html


class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
        self.question = None

    def next_question(self):
        self.question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.question.text)
        return f"Q.{self.question_number}: {q_text}"

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        correct_answer = self.question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
