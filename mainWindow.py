import tkinter as tk

win = tk.Tk()
win.geometry("1400x780+60+10")
win.resizable(0, 0)
win.title("Course Selection Supporting System")

userData = tk.LabelFrame(text="PERSONAL DATA", font="TimesNewRoman 16 bold")
userData.config(height=220, width=400, relief="flat", bd=10)
userData.config(highlightbackground="#888888", highlightthickness=5)
userData.place(x=25, y=25)

userName = tk.Label(userData, text="● 姓名：吳承翰", font="標楷體")
userName.place(x=10, y=10)
userDepartment = tk.Label(userData, text="● 系級：經濟系 大一", font="標楷體")
userDepartment.place(x=10, y=35)
creditEarned = tk.Label(userData, text="● 已修習學分數：", font="標楷體")
creditEarned.place(x=10, y=60)
creditLack = tk.Label(userData, text="● 尚需學分數：", font="標楷體")
creditLack.place(x=10, y=110)

courseTable = tk.LabelFrame()
courseTable.config(height=675, width=540, relief="flat", bd=0)
courseTable.config(highlightbackground="#888888", highlightthickness=5)
courseTable.place(x=440, y=25)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
lessonCode = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "B", "C", "D"]
curriculum = []
for i in range(112):
    if i < 16:
        if int(i%16) == 0:
            curriculum.append(tk.Label(courseTable, text=""))
        else:
            curriculum.append(tk.Label(courseTable, text="%s"%lessonCode[i - 1], fg="#000000"))
    elif int(i%16) == 0:
        curriculum.append(tk.Label(courseTable, text="%s"%days[int(i/16) - 1], fg="#000000"))
    else:
        curriculum.append(tk.Button(courseTable, text=""))
    
    curriculum[i].config(height=2, width=11)
    curriculum[i].grid(row=int(i%16), column=int(i/16))

win.mainloop()