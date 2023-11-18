from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizApp")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_box = self.canvas.create_text(
            150,
            125,
            text="Question",
            width=280,
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.green_button)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.red_button)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        if self.quiz.still_has_question():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_box, text=q_text)
        else:
            self.canvas.itemconfig(self.question_box, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def green_button(self):
        is_correct = self.quiz.check_answer("True")
        self.true_button.config(state="disabled")
        self.feedback(is_correct)

    def red_button(self):
        is_correct = self.quiz.check_answer("False")
        self.false_button.config(state="disabled")
        self.feedback(is_correct)

    def feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
