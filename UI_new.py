import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
SCHOOL_YEAR = 109

def credit_no_credit(finished, required_subjects):
    # 回傳已經修了多少學分、剩餘必修學分、尚未完成必修
    # print(finished)
    # print(required_subjects)
    credit = 0
    notfinished = []
    no_credit = 0
    pastCourse = []
    for i in range(len(required_subjects)):
        if finished[required_subjects[i][0]] == 1:
            credit += int(required_subjects[i][1])
            pastCourse.append(required_subjects[i][0])
        else:
            notfinished.append(required_subjects[i][0])
            no_credit += int(required_subjects[i][1])
    return credit, no_credit, notfinished, pastCourse

class LoginWindow(tk.Frame):

    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        f1 = tkFont.Font(size = 24, family = "jf open 粉圓 1.1")
        f3 = tkFont.Font(size = 16, family = "標楷體")

        # self.cvsMain = tk.Canvas(self, width = 400, height = 300, bg = "white")
        self.lblExp = tk.Label(self, text = "歡迎使用修課檢驗系統，請在下方輸入您的姓名", height = 1, width = 40, font = f3)
        self.lblName = tk.Label(self, text = "姓名:", height = 1, width = 6, font = f3)
        self.txtName = tk.Text(self, height = 1, width = 8, font = f1)
        self.btnLogin = tk.Button(self, text = "登入/註冊", height = 1, width = 6, command = self.UserCheck, font = f3)

        self.lblExp.grid(row = 0, column = 0, columnspan = 4, sticky = tk.NE + tk.SW)
        # self.cvsMain.grid(row = 0, column = 0, columnspan = 3, sticky = tk.NE + tk.SW)
        self.lblName.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.txtName.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)
        self.btnLogin.grid(row = 2, column = 1, columnspan = 2, sticky = tk.NE + tk.SW)
    
    def UserCheck(self):
        user = self.txtName.get("1.0", "end-1c")
        self.user = user
        print(user)

        try:
            with open(file="name.txt", mode="r+", encoding="utf-8") as file:
                nameList = file.readlines()
            for i in range(len(nameList)):
                nameList[i] = nameList[i].rstrip("\n")
            
            if user in nameList:
                self.newUser = False
                self.master.destroy()
            else:
                self.newUser = True
                self.signUpWin = tk.Toplevel(self.master)
                self.signUp = SignUpWindow(self.signUpWin, user)
        except:
            with open(file="name.txt", mode="w", encoding="utf-8") as file:
                print("New file")
            self.newUser = True
            self.signUpWin = tk.Toplevel(self)
            self.signUp = SignUpWindow(self.signUpWin, user)

        
    def openMain(self):
        self.newWindow = tk.Toplevel()
    
class SignUpWindow(tk.Frame):

    def __init__(self, master, user):
        self.master = master
        self.user = user
        self.master.geometry('+500+400')
        self.createWindow()

    def createWindow(self):
        f3 = tkFont.Font(size = 16, family = "標楷體")

        self.lblSignExp = tk.Label(self.master, text = "第一次見到您，讓我們來為您建立你專屬的修課紀錄！", height = 1, width = 40, font = f3)
        self.lblSignName = tk.Label(self.master, text = "姓名:", height = 1, width = 6, font = f3)
        self.txtSignName = tk.Text(self.master, height = 1, width = 8, font = f3)
        self.lblSignDpt = tk.Label(self.master, text = "學系:", height = 1, width = 6, font = f3)
        self.comboDpt = ttk.Combobox(self.master, values = ["經濟", "政治", "財金", "國企", "工管", "資管"], height = 5, width = 8, font = f3)
        self.lblSignYear = tk.Label(self.master, text = "入學學年:", height = 1, width = 6, font = f3)
        self.comboYear = ttk.Combobox(self.master, values = ["109", "108", "107", "106", "105"], height = 5, width = 8, font = f3)
        self.btnApply = tk.Button(self.master, text = "註冊", height = 1, width = 6, command = self.UserInfo, font = f3)

        self.lblSignExp.grid(row = 0, column = 0, columnspan = 4, sticky = tk.NE + tk.SW)
        self.lblSignName.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.txtSignName.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)
        self.lblSignDpt.grid(row = 2, column = 1, sticky = tk.NE + tk.SW)
        self.comboDpt.grid(row = 2, column = 2, sticky = tk.NE + tk.SW)
        self.lblSignYear.grid(row = 3, column = 1, sticky = tk.NE + tk.SW)
        self.comboYear.grid(row = 3, column = 2, sticky = tk.NE + tk.SW)
        self.btnApply.grid(row = 4, column = 1, columnspan = 2, sticky = tk.NE + tk.SW)

        self.txtSignName.insert(1.0, self.user)

    def UserInfo(self):
        name = self.txtSignName.get("1.0", "end-1c")
        self.master = name
        department = self.comboDpt.get()
        year = self.comboYear.get()
        print(name, department, year)
        with open(file="name.txt", mode="a", encoding="utf-8") as file:
            file.write(name + "\n")
        with open(file="%s.txt" %name, mode="w", encoding="utf-8") as file:
            file.write("%s,%s\n" %(department, year))
        
        tk.messagebox.showinfo('註冊','已替您建立您的帳戶')
        root.destroy()

class MainWindow(tk.Frame):

    def __init__(self, master, user):
        self.master = master
        self.user = user
        self.createWindow()
    
    def courseShow(self):
        for i in range(17, 112):
            if i % 16 != 0:
                self.curriculum[i].config(text="", bg=self.defaultBG)
        for i in range(len(self.pastCourse)):
            for j in range(len(self.required_subjects)):
                if(self.required_subjects[j][0] == self.pastCourse[i] and
                   int(int(self.required_subjects[j][2]) / 10) == self.gradeDisplay and
                   int(int(self.required_subjects[j][2]) % 10) == self.semesterDisplay):
                    a = self.required_subjects[j][3].split(",")
                    for k in range(int(len(a) / 2)):
                        for m in range(int(a[k * 2 + 1])):
                            self.curriculum[int(a[k * 2]) + m].config(text="%s"%self.required_subjects[j][0])
                    break
        self.yearLabel.config(text="%s%s"%(self.gradeTrans[self.gradeDisplay], self.semesterTrans[self.semesterDisplay]))
    
    def lastSemester(self):
        self.semesterDisplay = self.semesterDisplay % 2 + 1
        if self.semesterDisplay == 2:
            self.gradeDisplay -= 1
        self.courseShow()
        
        if self.gradeDisplay == 1 and self.semesterDisplay == 1:
            self.lastSemesterBtn.config(state="disabled")
        if self.gradeDisplay == 4 and self.semesterDisplay == 1:
            self.nextSemesterBtn.config(state="normal")
    
    def nextSemester(self):
        self.semesterDisplay = self.semesterDisplay % 2 + 1
        if self.semesterDisplay == 1:
            self.gradeDisplay += 1
        self.courseShow()
        
        if self.gradeDisplay == 4 and self.semesterDisplay == 2:
            self.nextSemesterBtn.config(state="disabled")
        if self.gradeDisplay == 1 and self.semesterDisplay == 2:
            self.lastSemesterBtn.config(state="normal")
    
    def high_light_course(self, event):
        for i in range(17, 112):
            if i % 16 != 0:
                self.curriculum[i].config(bg=self.defaultBG)
        courseName = self.unchosenCourse.get(self.unchosenCourse.curselection())
        for i in range(len(self.required_subjects)):
            if self.required_subjects[i][0] == courseName:
                if(self.gradeDisplay == int(int(self.required_subjects[i][2]) / 10) and
                   self.semesterDisplay == int(int(self.required_subjects[i][2]) % 10)):
                    a = self.required_subjects[i][3].split(",")
                    for j in range(int(len(a) / 2)):
                        for k in range(int(a[j * 2 + 1])):
                            self.curriculum[int(a[j * 2]) + k].config(bg="red")
    
    def cancel(self):
        for i in range(17, 112):
            if i % 16 != 0:
                self.curriculum[i].config(bg=self.defaultBG)
    
    def createWindow(self):
        
        self.courseData()
        self.userData = tk.LabelFrame(text="PERSONAL DATA", font="TimesNewRoman 16 bold")
        self.userData.config(height=220, width=600, relief="flat", bd=10)
        self.userData.config(highlightbackground="#888888", highlightthickness=5)
        self.userData.place(x=45, y=40)
        self.defaultBG = self.userData.cget("bg")

        self.userName = tk.Label(self.userData, text="● 姓名：%s" %self.user, font="標楷體")
        self.userName.place(x=10, y=10)
        self.userDpt = tk.Label(self.userData, text="● 系級：%s系 %s" %(self.department, self.userGrade), font="標楷體")
        self.userDpt.place(x=10, y=35)
        self.creditEarned = tk.Label(self.userData, text="● 已修習學分數：%s" %self.credit, font="標楷體")
        self.creditEarned.place(x=10, y=60)
        self.creditLack = tk.Label(self.userData, text="● 尚需學分數： %s" %self.no_credit, font="標楷體")
        self.creditLack.place(x=10, y=110)
        
        self.semesterDisplay  = 1
        self.gradeDisplay = SCHOOL_YEAR - int(self.year) + 1
        self.courseTable = tk.LabelFrame()
        self.courseTable.config(height=675, width=540, relief="flat", bd=0)
        self.courseTable.config(highlightbackground="#888888", highlightthickness=5)
        self.courseTable.place(x=680, y=40)
        self.lastSemesterBtn = tk.Button(text="⇦", font="標楷體 24 bold", relief="flat", command=self.lastSemester)
        self.lastSemesterBtn.place(x=900, y=735, anchor=tk.CENTER)
        self.nextSemesterBtn = tk.Button(text="⇨", font="標楷體 24 bold", relief="flat", command=self.nextSemester)
        self.nextSemesterBtn.place(x=1120, y=735, anchor=tk.CENTER)
        self.yearLabel = tk.Label(text="", font="標楷體 20")
        self.yearLabel.place(x=1010, y=735, anchor=tk.CENTER)

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        lessonCode = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "B", "C", "D"]
        self.curriculum = []
        for i in range(112):
            if i < 16:
                if int(i%16) == 0:
                    self.curriculum.append(tk.Label(self.courseTable, text=""))
                else:
                    self.curriculum.append(tk.Label(self.courseTable, text="%s"%lessonCode[i - 1], fg="#000000"))
            elif int(i%16) == 0:
                self.curriculum.append(tk.Label(self.courseTable, text="%s"%days[int(i/16) - 1], fg="#000000"))
            else:
                self.curriculum.append(tk.Button(self.courseTable, text="", fg="#000000", wraplength=70))
            
            self.curriculum[i].config(height=2, width=12)
            self.curriculum[i].grid(row=int(i%16), column=int(i/16))
        
        self.courseShow()
        if self.gradeDisplay == 1:
            self.lastSemesterBtn.config(state="disabled")
        
        self.leftFrame = tk.LabelFrame()
        self.leftFrame.config(height=200, width=200, relief="flat", bd=0)
        self.leftFrame.config(highlightbackground="#888888", highlightthickness=3)
        self.leftFrame.place(x=45, y=300)
        self.sb1 = tk.Scrollbar(self.leftFrame)
        self.sb1.pack(side="right", fill="y")
        self.unchosenCourse = tk.Listbox(self.leftFrame, width=20, height=10, yscrollcommand=self.sb1.set)
        self.unchosenCourse.pack(side="left")
        self.sb1.config(command=self.unchosenCourse.yview)
        for i in range(len(self.required_subjects)):
            for j in range(len(self.pastCourse)):
                # if self.required_subjects[i][0] == self.pastCourse[j]:
                    # break
                # elif j == len(self.pastCourse) - 1:
                self.unchosenCourse.insert("end", self.pastCourse[j])
        self.unchosenCourse.bind("<ButtonRelease-1>", self.high_light_course)
        
        self.cancelBtn = tk.Button(text="取消", height=1, width=10, command=self.cancel)
        self.cancelBtn.place(x=45, y=600)
        
    def courseData(self):

        with open(file="%s.txt" %self.user, mode="r", encoding="utf-8") as file:
            data = file.readline().rstrip("\n").split(",")
        
        self.department = data[0]
        self.year = data[1]
        self.grade = {"109":"大一", "108":"大二", "107":"大三", "106":"大四", "105":"大五"}
        self.userGrade = self.grade[self.year]
        self.semesterTrans = {1:"上", 2:"下"}
        self.gradeTrans = {1:"大一", 2:"大二", 3:"大三", 4:"大四"}
        
        # 載入該系必修、選修資料庫
        with open(file="%s%s.txt" %(self.department, self.year), mode="r", encoding="utf-8") as file:
            line = file.readline().rstrip("\n").split()
            if line[0] == self.department and line[1] == self.year:
                print("已替您載入%s系 %s學年度必修與選修資料庫" %(self.department, self.year))
            required = file.readline().split()
            required_credit = required[1]
            required_subjects = []
            
            while(True):
                a = file.readline().split()
                if a[0] == "系定選修":
                    elective_credit = a[1]
                    break
                required_subjects.append(a)
            # print(required_subjects)
        self.required_subjects = required_subjects

        # 建立已完成課程名單
        finished = dict()
        for i in range(len(required_subjects)):
            finished[required_subjects[i][0]] = 0

        with open(file="%s.txt" %self.user, mode="r", encoding="utf-8") as file:
            line = file.readline().rstrip("\n").split(",")
            print("您是%s系%s年入學的，已替您載入你專屬的修課紀錄" %(self.department, self.year))
            for line in file:
                line = line.strip("\n")
                finished[line] = 1

        # 計算已修的必修課程學分數、剩餘必修學分、未完成必修課
        self.credit, self.no_credit, self.not_finished, self.pastCourse = credit_no_credit(finished, required_subjects)
        print(self.credit, self.no_credit, self.not_finished, self.pastCourse)

appUser = ""
root = tk.Tk()
root.geometry('+500+400')  
app = LoginWindow(root)
app.master.title("台大修課檢驗系統")
app.mainloop()

print(type(app.master))

if app.newUser == True:
    win = tk.Tk()
    win.geometry("1400x780+60+10")
    main = MainWindow(win, app.signUp.user)
    win.title("Course Selection Supporting System")
else:
    win = tk.Tk()
    win.geometry("1400x780+60+10")
    main = MainWindow(win, app.user)
    win.title("Course Selection Supporting System")




win.mainloop()