from tkinter import *
from tkinter import messagebox
import webbrowser



root = Tk()
root.title('Microsoft Error')


def Popup():
   respone =  messagebox.showwarning('System Warning', "Virus Detected")
   if respone == "ok":
       support = messagebox.showwarning(
           'Virus Detected',
        "Please contact support at microsofsupport@support or 020 500 1500")
       Label(root, text=support).pack()

       if support == "ok":
           webbrowser.open("https://support.microsoft.com/nl-nl")
           quit()


Button(root, text="Check For Virus", command=Popup).pack()

root.mainloop()