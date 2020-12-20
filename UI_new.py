import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox

class LoginWindow(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        f1 = tkFont.Font(size = 24, family = "jf open 粉圓 1.1")
        f2 = tkFont.Font(size = 32, family = "jf open 粉圓 1.1")
        f3 = tkFont.Font(size = 16, family = "jf open 粉圓 1.1")

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
        print(user)
        self.newUser = False
        with open(file="name.txt", mode="r+", encoding="utf-8") as file:
            nameList = file.readlines()

        for i in range(len(nameList)):
            nameList[i] = nameList[i].rstrip("\n")
        print(nameList)
        if user in nameList:
            print("True")
            self.newUser = False
            self.openMain()
        else:
            print(False)
            self.newUser = True
            with open(file="name.txt", mode="a", encoding="utf-8") as file:
                file.write(user + "\n")
            self.signUp()

    def openMain(self):
        self.newWindow = tk.Toplevel()
    
    def signUp(self):
        f3 = tkFont.Font(size = 16, family = "jf open 粉圓 1.1")

        self.signUpWin = tk.Toplevel(LoginWindow())
        window = self.signUpWin
        window.lblSignExp = tk.Label(window, text = "第一次見到您，讓我們來為您建立你專屬的修課紀錄！", height = 1, width = 40, font = f3)
        window.lblSignName = tk.Label(window, text = "姓名:", height = 1, width = 6, font = f3)
        window.txtSignName = tk.Text(window, height = 1, width = 8, font = f3)
        window.lblSignDpt = tk.Label(window, text = "學系:", height = 1, width = 6, font = f3)
        window.txtSignDpt = tk.Text(window, height = 1, width = 8, font = f3)
        window.lblSignYear = tk.Label(window, text = "入學學年:", height = 1, width = 6, font = f3)
        window.txtSignYear = tk.Text(window, height = 1, width = 8, font = f3)
        window.btnLogin2 = tk.Button(window, text = "登入/註冊", height = 1, width = 6, command = self.UserInfo, font = f3)

        window.lblSignExp.grid(row = 0, column = 0, columnspan = 4, sticky = tk.NE + tk.SW)
        window.lblSignName.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        window.txtSignName.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)
        window.lblSignDpt.grid(row = 2, column = 1, sticky = tk.NE + tk.SW)
        window.txtSignDpt.grid(row = 2, column = 2, sticky = tk.NE + tk.SW)
        window.lblSignYear.grid(row = 3, column = 1, sticky = tk.NE + tk.SW)
        window.txtSignYear.grid(row = 3, column = 2, sticky = tk.NE + tk.SW)
        window.btnLogin2.grid(row = 4, column = 1, columnspan = 2, sticky = tk.NE + tk.SW)

    def UserInfo(self):
        name = self.signUpWin.txtSignName.get("1.0", "end-1c")
        department = self.signUpWin.txtSignDpt.get("1.0", "end-1c")
        year = self.signUpWin.txtSignYear.get("1.0", "end-1c")
        print(name, department, year)
        self.newUser = False
        with open(file="%s.txt" %name, mode="w", encoding="utf-8") as file:
            file.write("%s,%s\n" %(department, year))
        
        tk.messagebox.showinfo('註冊','已替您建立您的帳戶')
        self.signUpWin.destroy()

        


pl = LoginWindow()
pl.master.title("台大修課檢驗系統")
pl.mainloop()
