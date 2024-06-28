import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#006769"
LTGREEN = "#9DDE8B"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20

reps = 1
check_marks = " "
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, check_marks
    window.after_cancel(timer)
    checks.config(text=" ")
    check_marks = ""
    reps = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, check_marks
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # calling the count down function, and setting up the times

    if reps % 2 == 0 and reps != 8:
        timer_label.config(text="short break")
        count_down(short_break_sec)
        reps += 1

    elif reps == 8:
        timer_label.config(text="long break")
        count_down(long_break_sec)
        reps += 1

    else:
        timer_label.config(text="work time!")
        count_down(work_sec)
        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    # get the closest whole number, if input = 4.8 then output = 4
    count_sec = count % 60

    # setting up the formatting for the timer using dynamic typing and f strings
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min == 0:
        count_min = "00"
    elif count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # setting up check marks
        check_marks = ""
        completed_sessions = math.floor(reps/2)
        for i in range(completed_sessions):
            check_marks += "✅ "
        checks.config(text=check_marks)



# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.minsize(width=400, height=300)
window.config(padx=100, pady=50, bg=LTGREEN)


# ---- Row 0 ---- #
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=LTGREEN)
timer_label.grid(column=1, row=0, sticky="N")


# ---- Row 1 ---- #
# setting up the background graphic, canvas can layer things over each other
canvas = tk.Canvas(width=200, height=224, bg=LTGREEN, highlightthickness=0)
# highlightthickness = 0 is used to remove the outline around the image

tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img,)

# putting counter on the tomato
timer_text = canvas.create_text(105, 130, text="00:00",  font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)


# ---- Row 2 ---- #
button_start = tk.Button(text="Start", fg=GREEN, bg=LTGREEN, font=(FONT_NAME, 20), highlightthickness=0, command=start_timer)
# remember to call a function use command=<function name>, do not put the ()
button_start.grid(column=0, row=2, sticky="S")

# setting up a string var to hold the checkmarks
checks = tk.Label(text=" ", bg=LTGREEN)
checks.grid(column=1, row=2, sticky="S")

button_stop = tk.Button(text="Stop", fg=GREEN, bg=LTGREEN, font=(FONT_NAME, 20), highlightthickness=0, command=reset_timer)
button_stop.grid(column=2, row=2, sticky="S")


window.mainloop()
