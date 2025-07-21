# To create our UI
# to visualize our Interface
from tkinter import *
from quiz_brain import QuizBrain

#or we can cutomize our Own color
THEME_COLOR = "#000000"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain): # to import this properly
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QUIZ GAME")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")) # adjusting width here
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.right_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.wrong_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="yellow") # if we reach end of quiz
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="you have reached the limit 10/10 quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")# when button got disappeared when the quiz ends

    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        right = self.quiz.check_answer("False")
        self.give_feedback(right)

    def give_feedback(self, right):
        if right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
