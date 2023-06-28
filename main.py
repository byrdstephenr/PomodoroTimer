from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #timer text
    canvas.itemconfig(timer_text, text="00:00" )
    #title_label
    title.config(text="Timer")
    #reset checkmarks
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        #8th
        count_down(long_break)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # 2nd/4th/6th
        count_down(short_break)
        title.config(text="Break", fg=PINK)
    else:
        # 1st/3rd/5th/7th timers
        count_down(work_min)
        title.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        total_checkmarks = CHECKMARK * (reps // 2)
        checkmark.config(text=total_checkmarks)
        print(reps)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)
window.config(width=600, height=600, background=YELLOW)


title = Label(text="Timer", foreground=GREEN)
title.config(font=(FONT_NAME, 50), background=YELLOW, highlightthickness=0)
title.grid(column=1, row=0)


canvas = Canvas(height=230, width=204, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(104, 115, image=tomato_img)
timer_text = canvas.create_text(104, 136, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


checkmark = Label(foreground=GREEN)
checkmark.config(font=(FONT_NAME, 10), background=YELLOW, highlightthickness=0)
checkmark.grid(column=1, row=3)

window.mainloop()