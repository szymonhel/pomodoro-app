import math
from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

window = Tk()


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_brake_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_brake_seconds)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


def pad_left(val):
    if val < 10:
        return f"0{val}"
    return val


def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    count_minute = pad_left(count_minute)
    count_seconds = pad_left(count_seconds)

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"

        check_mark.config(text=marks)


window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file='./tomato.png')
canvas.create_image(103, 109, image=photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start")
start_button.grid(column=0, row=2)
start_button.config(command=start_timer)
reset_button = Button(text="reset")
reset_button.grid(column=2, row=2)
reset_button.config(command=reset_timer)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)

window.mainloop()
