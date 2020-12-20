import tkinter as tk

win = tk.Tk()
win.geometry("1000x600+250+100")
win.resizable(0, 0)
win.title("Course Selection Supporting System")

userName = tk.Label(text="● 姓名：吳承翰", font="標楷體")
userName.place(x=20, y=25)
userDepartment = tk.Label(text="● 系級：經濟系 大一", font="標楷體")
userDepartment.place(x=20, y=50)
creditEarned = tk.Label(text="● 已修習學分數：", font="標楷體")
creditEarned.place(x=20, y=75)
creditLack = tk.Label(text="● 尚需學分數：", font="標楷體")
creditLack.place(x=20, y=125)




win.mainloop()