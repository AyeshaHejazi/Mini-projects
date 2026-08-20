#IMPORT LIBRARIES 
from tkinter import *
from tkinter import messagebox
import datetime
import time
import winsound
from threading import Thread

# WINDOW SETUP 
root = Tk()
root.title("Eric's Alarm Clock")
root.geometry("450x300")
root.config(bg="black")

# ALARM FUNCTION 
def start_alarm():
    t1 = Thread(target=alarm)
    t1.daemon = True
    t1.start()

def alarm():
    while True:

        # Current selected alarm time
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Current system time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # Show time in console
        print("Current Time:", current_time)
        print("Alarm Time:", set_alarm_time)

        # Check alarm
        if current_time == set_alarm_time:

            # Popup Message
            messagebox.showinfo("WAKE UP!", "TIME TO WAKE UP!")

            # Loud Beep Sound
            for i in range(5):
                winsound.Beep(2500, 1000)

            break

        time.sleep(1)

#  HEADING 
Label(
    root,
    text="ALARM CLOCK",
    font=("Helvetica", 24, "bold"),
    fg="cyan",
    bg="black"
).pack(pady=20)

#  FRAME FOR OPTIONS
frame = Frame(root, bg="black")
frame.pack()

# HOURS 
hour = StringVar(root)
hours = [f"{i:02}" for i in range(24)]
hour.set(hours[0])

OptionMenu(frame, hour, *hours).pack(side=LEFT, padx=10)

# MINUTES 
minute = StringVar(root)
minutes = [f"{i:02}" for i in range(60)]
minute.set(minutes[0])

OptionMenu(frame, minute, *minutes).pack(side=LEFT, padx=10)

#  SECONDS 
second = StringVar(root)
seconds = [f"{i:02}" for i in range(60)]
second.set(seconds[0])

OptionMenu(frame, second, *seconds).pack(side=LEFT, padx=10)

#  BUTTON TO SET ALARM
Button(
    root,
    text="SET ALARM",
    font=("Helvetica", 15, "bold"),
    bg="red",
    fg="white",
    padx=10,
    pady=5,
    command=start_alarm
).pack(pady=40)

root.mainloop()