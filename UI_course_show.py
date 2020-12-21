import tkinter as tk

def input_courses(name, department, year, new):
    # 增加新的修課
    time = ["大一上", "大一下", "大二上", "大二下", "大三上", "大三下", "大四上", "大四下"]
    with open(file="%s.txt" %name, mode="a", encoding="utf-8") as file:
        if new == 1:
            file.write("%s,%s\n" %(department, year))
        finish = False
        while(finish == 0):
            enter = input("請輸入課程全名，輸入「結束」來停止紀錄：")
            if enter == "結束":
                break
            file.write(enter + "\n")
            if enter in time:
                print("好的，%s" %enter)
            else:
                print("已紀錄%s" %enter, end=" ")
        print()
    return

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
    

print("歡迎使用修課檢驗系統")
name = input("請輸入您的姓名：")
newUser = False
# f = open(file="name.txt", mode="w", encoding="utf-8")
# f.close
with open(file="name.txt", mode="r+", encoding="utf-8") as file:
    nameList = file.readlines()

    for i in range(len(nameList)):
        nameList[i] = nameList[i].rstrip("\n")
    if name in nameList:
        print("\n%s，很高興再次見到您，我們已經有您先前的修課資訊" %name)
        with open(file="%s.txt" %name, mode="r", encoding="utf-8") as f:
            line = f.readline().rstrip("\n").split(",")
            department = line[0]
            year = line[1]
            print()
    else:
        file.write(name + "\n")
        print("\n第一次見到您，讓我們來為您建立你專屬的修課紀錄！")
        newUser = True

# 為新使用者建立資料
pastCourse = []
if newUser == 1:
    department = input("請輸入您的系別：")
    department = "經濟"
    year = input("請輸入您的入學年份（民國）：")
    year = "109"
    finish = False
    input_courses(name, department, year, newUser)
    newUser = False
    print("已經替您完成建檔")

# 載入該系必修、選修資料庫
with open(file="%s%s.txt" %(department, year), mode="r", encoding="utf-8") as file:
    line = file.readline().rstrip("\n").split()
    if line[0] == department and line[1] == year:
        print("已替您載入%s系 %s學年度必修與選修資料庫" %(department, year))
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

# 建立已完成課程名單
finished = dict()
for i in range(len(required_subjects)):
    finished[required_subjects[i][0]] = 0

with open(file="%s.txt" %name, mode="r", encoding="utf-8") as file:
    line = file.readline().rstrip("\n").split(",")
    department = line[0]
    year = line[1]
    print("您是%s系%s年入學的，已替您載入你專屬的修課紀錄" %(department, year))
    for line in file:
        line = line.strip("\n")
        finished[line] = 1

# 計算已修的必修課程學分數、剩餘必修學分、未完成必修課
credit, no_credit, not_finished, pastCourse = credit_no_credit(finished, required_subjects)

# 自此行程式起為UI
win = tk.Tk()
win.geometry("1400x780+60+10")
win.resizable(0, 0)
win.title("Course Selection Supporting System")

userData = tk.LabelFrame(text="PERSONAL DATA", font="TimesNewRoman 16 bold")
userData.config(height=220, width=400, relief="flat", bd=10)
userData.config(highlightbackground="#888888", highlightthickness=5)
userData.place(x=25, y=25)

# 更改此block共4個label的text的顯示內容
userName = tk.Label(userData, text="● 姓名：%s"%name, font="標楷體")
userName.place(x=10, y=10)
userDepartment = tk.Label(userData, text="● 系級：%s系 %s年入學"%(department, year), font="標楷體")
userDepartment.place(x=10, y=35)
creditEarned = tk.Label(userData, text="● 已修習學分數：%d"%credit, font="標楷體")
creditEarned.place(x=10, y=60)
creditLack = tk.Label(userData, text="● 尚需學分數：%d"%no_credit, font="標楷體")
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
        # 加上fg和wraplength
        curriculum.append(tk.Button(courseTable, text="", fg="#000000", wraplength=70))
    
    curriculum[i].config(height=2, width=11)
    curriculum[i].grid(row=int(i%16), column=int(i/16))

# 課程顯示 (未加入學年的選擇)
for i in range(len(pastCourse)):
    for j in range(len(required_subjects)):
        if(required_subjects[j][0] == pastCourse[i]):
            for i in range(int(required_subjects[j][1])):
                curriculum[int(required_subjects[j][3]) + i].config(text="%s"%required_subjects[j][0])
            break

win.mainloop()




print("\n您已有%d學分的必修課完成" %credit)
print("您尚有%d學分的必修課未完成" %no_credit)
print("尚要完成的必修課：", end="")
for i in range(len(not_finished) - 1):
    print(not_finished[i], end=",")
print(not_finished[-1])

see = input("要看之前您已經修了什麼課嗎？ 輸入是/否：")
if see == "是":
    print("\n您已經修了以下課程：")
    for i in range(len(pastCourse)):
        for j in range(len(required_subjects)):
            if(required_subjects[j] == pastCourse[i]):
                curriculum[int(required_subjects[j][3])](text="456")

while(True):
    more = input("請問有新的課程要加入嗎？ 輸入是/否：")
    if more == "是":
        input_courses(name, department, year, newUser)
        # 更新已修課程紀錄，來輸出完成及未完成學分
        with open(file="./%s.txt" %name, mode="r", encoding="utf-8") as file:
            line = file.readline().rstrip("\n").split(",")
            for line in file:
                line = line.strip("\n")
                finished[line] = 1

        credit, no_credit, not_finished, pastCourse = credit_no_credit(finished, required_subjects)
        print("您已有%d學分的必修課完成" %credit)
        print("您尚有%d學分的必修課未完成" %no_credit)
        print("尚要完成的必修課：", end="")
        for i in range(len(not_finished) - 1):
            print(not_finished[i], end=",")
        print(not_finished[-1])
        see = input("要確認加入後的修課紀錄嗎？ 輸入是/否：")
        if see == "是":
            print("\n您已經修了以下課程：")
            for i in range(len(pastCourse)):
                print(pastCourse[i])
    else:
        break

print("\n感謝您的使用")
