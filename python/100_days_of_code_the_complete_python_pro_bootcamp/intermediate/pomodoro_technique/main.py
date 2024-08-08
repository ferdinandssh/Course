from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.2
IMG_PATH = "/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/pomodoro_technique/tomato.png"
reps = 0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps=0
    title_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text=f'00:00')
    check_mark.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_seconds = WORK_MIN*60
    short_break_seconds = SHORT_BREAK_MIN*60
    long_break_seconds = LONG_BREAK_MIN*60
    if reps%8 == 0:
        countdown(long_break_seconds)
        title_label.config(text="Long break",fg=RED)
    elif reps%2 == 0:
        countdown(short_break_seconds)
        title_label.config(text="Short break",fg=YELLOW)
    else:
        countdown(work_seconds)
        title_label.config(text="Work",fg=GREEN)        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    minutes = math.floor(count/60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = count%60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text,text=f'{minutes}:{seconds}')
    if count>0:        
        timer = window.after(1000,countdown,count-1)        
    else:
        start_timer()
        mark=''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += '✓'                
        check_mark.config(text=mark)
        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=300, height=300)
window.config(padx=100,pady=50,bg=PINK)    

title_label = Label(text="Timer",fg=GREEN,bg=PINK,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
img_number = PhotoImage(file=IMG_PATH)
canvas.create_image(100,112,image=img_number)
timer_text = canvas.create_text(100,130,text = "00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="Start",bg=PINK,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",bg=PINK,highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark = Label(text="",bg=PINK,fg=GREEN)
check_mark.grid(column=1,row=3)



window.mainloop()


