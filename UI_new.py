import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk


class LoginWindow(tk.Frame):

    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        f1 = tkFont.Font(size = 24, family = "jf open 粉圓 1.1")
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

        try:
            with open(file="name.txt", mode="r+", encoding="utf-8") as file:
                nameList = file.readlines()
            for i in range(len(nameList)):
                nameList[i] = nameList[i].rstrip("\n")
            
            if user in nameList:
                self.openMain()
            else:
                self.signUpWin = tk.Toplevel(self.master)
                self.app = SignUpWindow(self.signUpWin, user)
        except:
            with open(file="name.txt", mode="w", encoding="utf-8") as file:
                print("New file")
            self.signUpWin = tk.Toplevel(self)
            self.app = SignUpWindow(self.signUpWin, user)

        
    def openMain(self):
        self.newWindow = tk.Toplevel()
    
class SignUpWindow(tk.Frame):

    def __init__(self, master, user):
        self.master = master
        self.user = user
        self.createWindow()

    def createWindow(self):
        f3 = tkFont.Font(size = 16, family = "jf open 粉圓 1.1")

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
        department = self.comboDpt.get()
        year = self.comboYear.get()
        print(name, department, year)
        with open(file="name.txt", mode="a", encoding="utf-8") as file:
            file.write(name + "\n")
        with open(file="%s.txt" %name, mode="w", encoding="utf-8") as file:
            file.write("%s,%s\n" %(department, year))
        
        tk.messagebox.showinfo('註冊','已替您建立您的帳戶')
        self.master.destroy()


root = tk.Tk()
root.config(background="yellow")
app = LoginWindow(root)
app.master.title("台大修課檢驗系統")
app.mainloop()
