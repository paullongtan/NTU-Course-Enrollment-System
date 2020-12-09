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
        print(pastCourse[i])

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



        
        

    

