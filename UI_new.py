import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
SCHOOL_YEAR = 109

def credit_no_credit(user):
    # 回傳已經修了多少學分、剩餘必修學分、尚未完成必修
    with open(file="%s.txt" %user, mode="r", encoding="utf-8") as file:
        line = file.readline().rstrip("\n").split(",")
        department = line[0]
        year = line[1]

    with open(file="%s%s.txt" %(department, year), mode="r", encoding="utf-8") as file:
        line = file.readline().rstrip("\n").split()
        if line[0] == department and line[1] == year:
            print("已替您載入%s系 %s學年度必修與選修資料庫" %(department, year))
        
        file.readline()
        required_subjects = []
        while(True):
            a = file.readline().split()
            if a[0] == "系定必修":
                continue
            if a[0] == "系定選修":
                break
            required_subjects.append(a)

        # 建立已完成課程名單
        finished = dict()
        for i in range(len(required_subjects)):
            finished[required_subjects[i][0]] = 0
        

        with open(file="%s.txt" %user, mode="r", encoding="utf-8") as file:
            line = file.readline().rstrip("\n").split(",")
            for line in file:
                line = line.strip("\n")
                line = line.split()
                finished[line[0]] = "1%s"%line[1]

    credit = 0
    notfinished = []
    no_credit = 0
    pastCourse = []
    pastTime = []
    for i in range(len(required_subjects)):
        if int(finished[required_subjects[i][0]]) >= 100:
            credit += int(required_subjects[i][1])
            pastCourse.append(required_subjects[i][0])
            pastTime.append(int(finished[required_subjects[i][0]]) - 100)
        else:
            notfinished.append(required_subjects[i][0])
            no_credit += int(required_subjects[i][1])
    return credit, no_credit, notfinished, pastCourse, required_subjects, pastTime

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
        self.year = year
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
        tk.Frame.__init__(self)
        self.createWindow()
    
    def courseShow(self):
        for i in range(17, 112):
            if i % 16 != 0:
                self.curriculum[i].config(text="", bg=self.defaultBG)
        for i in range(len(self.pastCourse)):
            for j in range(len(self.required_subjects)):
                if(self.required_subjects[j][0] == self.pastCourse[i] and
                   int(int(self.pastTime[i]) / 10) == self.gradeDisplay and
                   int(int(self.pastTime[i]) % 10) == self.semesterDisplay):
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
        if self.unchosenCourse.curselection() != () or self.chosenCourse.curselection() != ():
            self.high_light_course("<ButtonRelease-1>")
    
    def nextSemester(self):
        self.semesterDisplay = self.semesterDisplay % 2 + 1
        if self.semesterDisplay == 1:
            self.gradeDisplay += 1
        self.courseShow()
        
        if self.gradeDisplay == 4 and self.semesterDisplay == 2:
            self.nextSemesterBtn.config(state="disabled")
        if self.gradeDisplay == 1 and self.semesterDisplay == 2:
            self.lastSemesterBtn.config(state="normal")
        if self.unchosenCourse.curselection() != () or self.chosenCourse.curselection() != ():
            self.high_light_course("<ButtonRelease-1>")
    
    def high_light_course(self, event):
        for i in range(17, 112):
            if i % 16 != 0:
                self.curriculum[i].config(bg=self.defaultBG)
        if self.unchosenCourse.curselection() != ():
            courseName = self.unchosenCourse.get(self.unchosenCourse.curselection())
        else:
            courseName = self.chosenCourse.get(self.chosenCourse.curselection())
        timeFree = "green"
        for i in range(len(self.required_subjects)):
            if self.required_subjects[i][0] == courseName:
                if (self.semesterDisplay == int(int(self.required_subjects[i][2]) % 10) and
                    (self.gradeDisplay >= int(int(self.required_subjects[i][2]) / 10))):
                    a = self.required_subjects[i][3].split(",")
                    for j in range(len(self.pastTime)):
                        if(self.pastCourse[j] == courseName and
                           self.gradeDisplay == int(int(self.pastTime[j]) / 10) and
                           self.semesterDisplay == int(int(self.pastTime[j]) % 10)):
                            timeFree = "yellow"
                            continue
                    if timeFree != "yellow":
                        for j in range(int(len(a) / 2)):
                            for k in range(int(a[j * 2 + 1])):
                                if(self.curriculum[int(a[j * 2]) + k].cget("text") != ""):
                                    timeFree = "red"
                                    break
                    for j in range(int(len(a) / 2)):
                        for k in range(int(a[j * 2 + 1])):
                            self.curriculum[int(a[j * 2]) + k].config(bg=timeFree)
                    break
    
    def cancel(self):
        for i in range(17, 112):
            if i % 16 != 0:
                self.curriculum[i].config(bg=self.defaultBG)
    
    def add_course(self):
        if self.unchosenCourse.curselection() != ():
            timeFree = True
            courseName = self.unchosenCourse.get(self.unchosenCourse.curselection())
            for i in range(len(self.required_subjects)):
                if self.required_subjects[i][0] == courseName:
                    conditionFit = (self.semesterDisplay == int(int(self.required_subjects[i][2]) % 10))
                    if conditionFit == True:
                        conditionFit = (self.gradeDisplay >= int(int(self.required_subjects[i][2]) / 10))
                        if conditionFit == True:              
                            b = self.required_subjects[i][4].split(",")
                            if conditionFit == True and b[0] != "無":
                                for j in range(len(b)):
                                    for k in range(len(self.pastCourse)):
                                        if self.pastCourse[k] == b[j]:
                                            break
                                        elif k == len(self.pastCourse) - 1:
                                            conditionFit = False
                                            self.error_message_precourse(b[j])
                        else:
                            self.error_message_grade(self.gradeTrans[int(int(self.required_subjects[i][2]) / 10)])
                    else:
                        self.error_message_semester(self.semesterTrans[int(int(self.required_subjects[i][2]) % 10)])
                    
                    a = self.required_subjects[i][3].split(",")
                    for j in range(int(len(a) / 2)):
                        for k in range(int(a[j * 2 + 1])):
                            if self.curriculum[int(a[j * 2]) + k].cget("text") != "":
                                timeFree = False
                                break
                        if timeFree == False:
                            self.error_message_time_conflict()
                            break
                    
                    if timeFree == True and conditionFit == True:
                        for j in range(int(len(a) / 2)):
                            for k in range(int(a[j * 2 + 1])):
                                self.curriculum[int(a[j * 2]) + k].config(text="%s"%self.required_subjects[i][0])
                        self.cancel()
                        self.unchosenCourse.delete(self.unchosenCourse.curselection())
                        self.not_finished.remove(courseName)
                        self.chosenCourse.insert("end", courseName)
                        self.pastCourse.append(courseName)
                        self.pastTime.append(self.gradeDisplay * 10 + self.semesterDisplay)
                        self.credit += int(self.required_subjects[i][1])
                        self.creditEarned.config(text="● 已修習學分數：%s" %self.credit)
                        self.no_credit -= int(self.required_subjects[i][1])
                        self.creditLack.config(text="● 尚需學分數： %s" %self.no_credit)
                    break
    
    def drop_course(self):
        if self.chosenCourse.curselection() != ():
            courseName = self.chosenCourse.get(self.chosenCourse.curselection())
            for i in range(len(self.pastCourse)):
                if self.pastCourse[i] == courseName:
                    if(self.gradeDisplay == int(int(self.pastTime[i]) / 10) and
                       self.semesterDisplay == int(int(self.pastTime[i]) % 10)):
                        for j in range(len(self.required_subjects)):
                            if self.required_subjects[j][0] == courseName:
                                a = self.required_subjects[j][3].split(",")
                                b = self.required_subjects[j][5].split(",")
                                break
                                
                        conditionFit = True
                        if b[0] != "無":
                            for j in range(len(b)):
                                for k in range(len(self.pastCourse)):
                                    if self.pastCourse[k] == b[j]:
                                        conditionFit = False
                                        self.error_message_postcourse(b[j])
                                        break
                                        
                        if conditionFit == True:
                            for j in range(int(len(a) / 2)):
                                for k in range(int(a[j * 2 + 1])):
                                    self.curriculum[int(a[j * 2]) + k].config(text="")
                            self.chosenCourse.delete(self.chosenCourse.curselection())
                            self.unchosenCourse.insert("end", courseName)
                            self.not_finished.append(courseName)
                            for j in range(len(self.pastCourse)):
                                if self.pastCourse[j] == courseName:
                                    self.pastCourse.pop(j)
                                    self.pastTime.pop(j)
                                    break
                            self.credit -= int(self.required_subjects[i][1])
                            self.creditEarned.config(text="● 已修習學分數：%s" %self.credit)
                            self.no_credit += int(self.required_subjects[i][1])
                            self.creditLack.config(text="● 尚需學分數： %s" %self.no_credit)
                            self.cancel()
                            self.courseShow()
                    else:
                        self.error_message_wrong_display(self.gradeTrans[int(int(self.pastTime[i]) / 10)], self.semesterTrans[int(int(self.pastTime[i]) % 10)])
                    break
                    
    def error_message_grade(self, limitGrade):
        tk.messagebox.showwarning("Error!", "年級未達%s無法修習此課程"%limitGrade)
    
    def error_message_semester(self, limitSemester):
        tk.messagebox.showwarning("Error!", "此課程開設時段為%s學期"%limitSemester)
    
    def error_message_precourse(self, preCourse):
        tk.messagebox.showwarning("Error!", "需先修習課程：%s"%preCourse)
    
    def error_message_time_conflict(self):
        tk.messagebox.showwarning("Error!", "修課時間重疊，請先退選原同時段課程")
        
    def error_message_wrong_display(self, courseGrade, courseSemester):
        tk.messagebox.showwarning("Error!", "請先將畫面移至修課時間：%s%s"%(courseGrade, courseSemester))
    
    def error_message_postcourse(self, postCourse):
        tk.messagebox.showwarning("Error!", "請先退選被擋修課程：%s"%postCourse)

    
    def addSelfCourse(self):
        self.selfCourseWin = tk.Toplevel(self)
        self.selfCourse = SelfCourseWindow(self.selfCourseWin, self.user)


    def end_system(self):
        with open(file="%s.txt" %self.user, mode="w", encoding="utf-8") as file:
            file.write(self.department + "," + self.year + "\n")
            for i in range(len(self.pastCourse)):
                file.write(self.pastCourse[i] + " " + str(self.pastTime[i]) + "\n")
        win.destroy()

    
    def createWindow(self):

        f1 = tkFont.Font(size = 16, family = "jf open 粉圓 1.1")
        f3 = tkFont.Font(size = 16, family = "標楷體")
        
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
        self.lastSemesterBtn.place(x=900, y=725, anchor=tk.CENTER)
        self.nextSemesterBtn = tk.Button(text="⇨", font="標楷體 24 bold", relief="flat", command=self.nextSemester)
        self.nextSemesterBtn.place(x=1120, y=725, anchor=tk.CENTER)
        self.yearLabel = tk.Label(text="", font="標楷體 20")
        self.yearLabel.place(x=1010, y=725, anchor=tk.CENTER)

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
                self.curriculum.append(tk.Label(self.courseTable, text="", fg="#000000", wraplength=70, bd=1, relief="ridge"))
            
            self.curriculum[i].config(height=2, width=12)
            self.curriculum[i].grid(row=int(i%16), column=int(i/16))
            self.curriculum[i].config(highlightthickness=2)
        
        self.courseShow()
        if self.gradeDisplay == 1:
            self.lastSemesterBtn.config(state="disabled")
        
        self.leftFrame = tk.LabelFrame(text="未選擇課程列表", font="標楷體 16")
        self.leftFrame.config(height=350, width=200, relief="flat", bd=0)
        self.leftFrame.config(highlightbackground="#888888", highlightthickness=3)
        self.leftFrame.place(x=45, y=280)
        self.sb1 = tk.Scrollbar(self.leftFrame)
        self.sb1.pack(side="right", fill="y")
        self.unchosenCourse = tk.Listbox(self.leftFrame, width=20, height=24, yscrollcommand=self.sb1.set)
        self.unchosenCourse.pack(side="left")
        self.sb1.config(command=self.unchosenCourse.yview)
        for i in self.not_finished:
                    self.unchosenCourse.insert("end", i)
        self.unchosenCourse.bind("<ButtonRelease-1>", self.high_light_course)
        
        self.leftCancelBtn = tk.Button(text="取消", height=1, width=8, command=self.cancel)
        self.leftCancelBtn.place(x=136, y=710)
        self.leftConfirmBtn = tk.Button(text="加選", height=1, width=8, command=self.add_course)
        self.leftConfirmBtn.place(x=52, y=710)
        
        self.rightFrame = tk.LabelFrame(text="已選擇課程列表", font="標楷體 16")
        self.rightFrame.config(height=350, width=200, relief="flat", bd=0)
        self.rightFrame.config(highlightbackground="#888888", highlightthickness=3)
        self.rightFrame.place(x=300, y=280)
        self.sb2 = tk.Scrollbar(self.rightFrame)
        self.sb2.pack(side="right", fill="y")
        self.chosenCourse = tk.Listbox(self.rightFrame, width=20, height=24, yscrollcommand=self.sb2.set)
        self.chosenCourse.pack(side="left")
        self.sb2.config(command=self.chosenCourse.yview)
        for i in range(len(self.pastCourse)):
            self.chosenCourse.insert("end", self.pastCourse[i])
        self.chosenCourse.bind("<ButtonRelease-1>", self.high_light_course)
        
        self.rightCancelBtn = tk.Button(text="取消", height=1, width=8, command=self.cancel)
        self.rightCancelBtn.place(x=391, y=710)
        self.rightConfirmBtn = tk.Button(text="退選", height=1, width=8, command=self.drop_course)
        self.rightConfirmBtn.place(x=307, y=710)

        self.selfCourseBtn = tk.Button(text="加入個人課程", height=2, width=10, font=f1, command=self.addSelfCourse)
        self.selfCourseBtn.place(x=50, y=220)
        
        self.endBtn = tk.Button(text="結束並存檔", pady=2, padx=2, command=self.end_system)
        self.endBtn.place(x=1250, y=725)
    
    def courseData(self):

        with open(file="%s.txt" %self.user, mode="r", encoding="utf-8") as file:
            data = file.readline().rstrip("\n").split(",")
        
        self.department = data[0]
        self.year = data[1]
        self.grade = {"109":"大一", "108":"大二", "107":"大三", "106":"大四", "105":"大五"}
        self.userGrade = self.grade[self.year]
        self.semesterTrans = {1:"上", 2:"下"}
        self.gradeTrans = {1:"大一", 2:"大二", 3:"大三", 4:"大四"}
        
        # 計算已修的必修課程學分數、剩餘必修學分、未完成必修課
        self.credit, self.no_credit, self.not_finished, self.pastCourse, self.required_subjects, self.pastTime = credit_no_credit(self.user)

    
class SelfCourseWindow(tk.Frame):

    def __init__(self, master, user):
        self.master = master
        self.user = user
        self.master.geometry('+500+300')
        self.createWindow()

    def createWindow(self):
        f3 = tkFont.Font(size = 16, family = "標楷體")

        self.lblSelfExp = tk.Label(self.master, text = "來加入你自己的專屬課程！", height = 1, width = 40, font = f3)
        self.lblCourseName = tk.Label(self.master, text = "課程名:", height = 1, width = 6, font = f3)
        self.txtCourseName = tk.Text(self.master, height = 1, width = 8, font = f3)
        self.lblCourseType = tk.Label(self.master, text = "課程類型:", height = 1, width = 6, font = f3)
        self.comboType = ttk.Combobox(self.master, values = ["系定選修", "一般選修", "共同必修", "體育", "其他"], height = 5, width = 8, font = f3)
        self.lblCredit = tk.Label(self.master, text = "學分數:", height = 1, width = 6, font = f3)
        self.comboCredit = ttk.Combobox(self.master, values = ["0", "1", "2", "3", "4", "5"], height = 5, width = 8, font = f3)
        self.lblCourseTime = tk.Label(self.master, text = "課程時間:", height = 1, width = 6, font = f3)
        self.comboSemester = ttk.Combobox(self.master, values = ["上學期", "下學期"], height = 5, width = 5, font = f3)
        self.comboWeekday = ttk.Combobox(self.master, values = ["週一", "週二", "週三", "週四", "週五"], height = 5, width = 5, font = f3)
        self.comboPeriod = ttk.Combobox(self.master, values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"], height = 8, width = 5, font = f3)
        self.btnAddTime = tk.Button(self.master, text = "加入時段", height = 1, width = 6, font = f3, command = self.addTime)
        self.btnApply = tk.Button(self.master, text = "加入課程", height = 1, width = 6, font = f3, command = self.addSelfCourse)
        self.lblTime = tk.Label(self.master, height = 1, width = 10, font = f3)
        self.lblCourse = tk.Label(self.master, height = 10, width = 10, font = f3)
        self.btnEndSection = tk.Button(self.master, text = "加入完成", height = 1, width = 6, font = f3, command = self.finishRecording)

        self.lblSelfExp.grid(row = 0, column = 0, columnspan = 4, sticky = tk.NE + tk.SW)
        self.lblCourseName.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.txtCourseName.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)
        self.lblCourseType.grid(row = 2, column = 1, sticky = tk.NE + tk.SW)
        self.comboType.grid(row = 2, column = 2, sticky = tk.NE + tk.SW)
        self.lblCredit.grid(row = 3, column = 1, sticky = tk.NE + tk.SW)
        self.comboCredit.grid(row = 3, column = 2, sticky = tk.NE + tk.SW)
        self.lblCourseTime.grid(row = 4, column = 1, sticky = tk.NE + tk.SW)
        self.comboSemester.grid(row = 4, column = 2, sticky = tk.NE + tk.SW)
        self.comboWeekday.grid(row = 5, column = 2, sticky = tk.NE + tk.SW)
        self.comboPeriod.grid(row = 6, column = 2, sticky = tk.NE + tk.SW)
        self.btnAddTime.grid(row = 7, column = 2, sticky = tk.NE + tk.SW)
        self.btnApply.grid(row = 8, column = 1, columnspan = 2, sticky = tk.NE + tk.SW)
        self.lblTime.grid(row = 9, column = 0, columnspan = 3, sticky = tk.NE + tk.SW)
        self.lblCourse.grid(row = 10, rowspan = 10, column = 0, columnspan = 8, sticky = tk.NE + tk.SW)
        self.btnEndSection.grid(row = 21, column = 9, sticky = tk.NE + tk.SW)
    
    def addTime(self):
        weekday = self.comboWeekday.get()
        period = self.comboPeriod.get()
        if len(self.lblTime.cget("text")) == 0:
            self.lblTime.configure(text = weekday + " " + period)
        else:
            self.lblTime.configure(text = self.lblTime.cget("text") + "," + weekday + " " + period)
    
    def addSelfCourse(self):
        toDay = {"週一":1, "週二":2, "週三":3, "週四":4, "週五":5}
        course = self.txtCourseName.get("1.0", "end-1c")
        courseType = self.comboType.get()
        courseCredit = self.comboCredit.get()
        semester = self.comboSemester.get()
        courseTime = self.lblTime.cget("text")
        time = courseTime.split(",")
        if len(self.lblCourse.cget("text")) == 0:
            self.lblCourse.configure(text = course)
        else:
            self.lblCourse.configure(text = self.lblCourse.cget("text") + "\n" + course)
        self.lblTime.configure(text = "")

        try:
            with open(file="%sSelfCourse.txt" %self.user, mode="a", encoding="utf-8") as file:
                file.write(course + " " + courseCredit + " ")
                period = []
                temp = ""
                for i in time:
                    a = i.split(" ")
                    temp += str(toDay[a[0]] * 16 + int(a[1]) + 1) + "," + "1" + " "
                temp = temp[0:-1]

                if semester == "上學期":
                    file.write("11" + " " + temp + " 無 無")
                else:
                    file.write("12" + " " + temp + " 無 無")
        except:
            with open(file="%sSelfCourse.txt" %self.user, mode="w", encoding="utf-8") as file:
                file.write(course + " " + courseCredit + " ")
                period = []
                temp = ""
                for i in time:
                    a = i.split(" ")
                    temp += str(toDay[a[0]] * 16 + int(a[1]) + 1) + "," + "1" + " "
                temp = temp[0:-1]

                if semester == "上學期":
                    file.write("11" + " " + temp + " 無 無")
                else:
                    file.write("12" + " " + temp + " 無 無")
    
    def finishRecording(self):
        self.master.destroy()

appUser = ""
root = tk.Tk()
root.geometry('+500+400')  
app = LoginWindow(root)
app.master.title("台大修課檢驗系統")
app.mainloop()

print(type(app.master))

win = tk.Tk()
win.geometry("1400x780+60+10")
main = MainWindow(win, app.user)
win.title("Course Selection Supporting System")


win.mainloop()