from tkinter import *
import datetime
import time
import winsound


# Часть 1: создание будильника

def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        msg = "Текущее время: " + str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
            break


def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{minute.get()}:{sec.get()}"
    Alarm(alarm_set_time)


# Часть 2: создание окна приложения
window = Tk()
window.title("Будильник")
window.geometry("400x160")
window.config(bg="#922B21")
window.resizable(width=False, height=False)

Label(window, text="Время должно быть установлено в 24-часовом формате!",
      fg="white", bg="#922B21",
      font=("Times New Roman", 12)).place(x=17, y=120)
Label(window, text="Часы         Мин         Сек", font=60,
      fg="white", bg="#922B21").place(x=210)
Label(window, text="Время для будильника: ",
      fg="white", bg="#922B21",
      font=("Times New Roman", 14)).place(x=10, y=40)

hour = StringVar()
minute = StringVar()
sec = StringVar()

Entry(window, textvariable=hour, bg="white", width=4,
      font=20).place(x=210, y=40)
Entry(window, textvariable=minute, bg="white", width=4,
      font=20).place(x=270, y=40)
Entry(window, textvariable=sec, bg="white", width=4,
      font=20).place(x=330, y=40)

Button(window, text="Вкл", fg="Black", bg="#D4AC0D",
       width=15, command=get_alarm_time,
       font=4).place(x=100, y=80)

window.mainloop()
