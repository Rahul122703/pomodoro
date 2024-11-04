from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
deciNumCount = 0
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BACKGROUND_COLOR = "#FFD700"
FONT_COLOR = "black"
second = 60
reps = 0
pomo = 0
mark = ""
timer = None
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_count(LONG_BREAK_MIN*60)
        timer_label.config(text="LONG BREAK", fg="blue")
    elif reps % 2 == 0:
        timer_count(SHORT_BREAK_MIN*60)
        timer_label.config(text="SHORT BREAK", fg="orange")
    else:
        timer_count(WORK_MIN*60)
        timer_label.config(text="!! WORK !!", fg="red")
# ---------------------------- TIMER RESET ------------------------------- #
def reset_all():
    global reps
    reps = 0
    timer_label.config(text="Timer", fg=FONT_COLOR)
    canvas.itemconfig(time_text, text="00:00")
    check_label.config(text=" ")
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_count(sec):
    minute = math.floor(sec/60)
    seconds = sec % 60
    if minute < 10:
        minute = f"0{minute}"
    if seconds < 10:
        seconds = f"0{seconds}"
    if sec > -1:
        canvas.itemconfig(time_text, text=f"{minute}:{seconds}")
        global timer
        timer = canvas.after(1000, timer_count, sec-1)
    else:
        global pomo, mark
        pomo += 1
        if pomo % 2 != 0:
            mark += "✔"
            check_label.config(text=mark)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO APP")
window.config(padx=80, pady=50, background=BACKGROUND_COLOR)

tomato_image = PhotoImage(file=r"G:\My Drive\WORK\MINE\Python\100 days python bootcamp\Day 28 (pomodoro)\tomato.png")

canvas = Canvas(width=200, height=224, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
time_text = canvas.create_text(103, 130, text=f"{WORK_MIN}:00", fill=FONT_COLOR, font=("Arial", 35, "bold"))

canvas.grid(row=1, column=1)

check_text = ""
check_label = Label(text=f"{check_text}", font=(FONT_NAME, 10, "bold"), bg=BACKGROUND_COLOR)
check_label.grid(row=3, column=1)

timer_label = Label(text=f"TIMER", font=(FONT_NAME, 30, "bold"), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
timer_label.grid(row=0, column=1)

start_button = Button(text="START",command=start_timer)
start_button.grid(row=2, column=0)

restart_button = Button(text="RESTART", command=reset_all)
restart_button.grid(row=2, column=3)

window.mainloop()
# ------------------------------------------------------------------- #

