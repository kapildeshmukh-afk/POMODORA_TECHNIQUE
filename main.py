from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
repeat = 0
timer = None
FONT = ("Courier", 35, "bold")
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_text.config(text="TIMER")
    check_marks.config(text="")
    global repeat
    repeat = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repeat
    repeat +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if repeat % 8 == 0:
        label_text.config(text="LONG BREAK", fg=RED)
        check_marks.config(text="✔")
        count_down(long_break_sec)
    elif repeat % 2 == 0:
        label_text.config(text="SHORT BREAK", fg=PINK)
        check_marks.config(text="✔")
        count_down(short_break_sec)
    else:
        label_text.config(text="WORK", fg=GREEN)
        check_marks.config(text="")
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min_count = math.floor(count/60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # mark = ""
        # workSession = math.floor(repeat/2)
        # for _ in range(workSession):
        #     mark += "✔"
        # check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORA")
window.config(padx=60, pady=60, bg=YELLOW)

label_text = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=FONT)
label_text.grid(column=1, row=0)
canvas = Canvas(height=224, width=210, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(106, 110, image=img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=FONT)
canvas.grid(column=1, row=1)

start_button = Button(text="START", bg="white", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="RESET", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
check_marks = Label( pady=30, fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)
window.mainloop()





