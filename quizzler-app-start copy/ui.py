from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title("Quiz_game")
        self.mainWindow.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="score:{0}", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="hgghhghghghcghcgh",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        true_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=true_image, highlightthickness=0)
        self.correct.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png",)
        self.wrong = Button(image=false_image, highlightthickness=0)
        self.wrong.grid(row=2, column=1,)

        self.mainWindow.mainloop()

