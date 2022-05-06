from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quizBrain:QuizBrain):
        self.quiz = quizBrain
        self.mainWindow = Tk()
        self.mainWindow.title("Quiz_game")
        self.mainWindow.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="hgghhghghghcghcgh",
                                                     width=200,
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        true_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.correct.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png",)
        self.wrong = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong.grid(row=2, column=1,)

        self.get_next_question()

        self.mainWindow.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="light green")
        else:
            self.canvas.config(bg="red")

        self.mainWindow.after(1000, self.get_next_question)