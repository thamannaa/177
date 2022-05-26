from tkinter import *
root=Tk()
root.title("Encapsulation")
root.geometry("600x600")

name_lbl=Label(root,text="name:")
name_lbl.place(relx=0.2,rely=0.1,anchor=CENTER)
name_input=Entry(root)
name_input.place(relx=0.4,rely=0.1,anchor=CENTER)

pass_lbl=Label(root,text="password:")
pass_lbl.place(relx=0.2,rely=0.3,anchor=CENTER)
pass_input=Entry(root)
pass_input.place(relx=0.4,rely=0.3,anchor=CENTER)

captcha_lbl=Label(root,text="captcha:")
captcha_lbl.place(relx=0.2,rely=0.5,anchor=CENTER)
captcha_input=Entry(root)
captcha_input.place(relx=0.4,rely=0.5,anchor=CENTER)

un_lbl=Label(root)
un_lbl.place(relx=0.5,rely=0.72,anchor=CENTER)

pword_show_lbl=Label(root)
pword_show_lbl.place(relx=0.5,rely=0.76,anchor=CENTER)

captcha_show_lbl=Label(root)
captcha_show_lbl.place(relx=0.5,rely=0.8,anchor=CENTER)

class user_db():
    def __init__(self):
        self.__username="thamannaa"
        self.__password="abcd@3"
        self.captcha="Aj7B"
        
    def show(self):
        un_lbl["text"]="name : "+self.__username
        pword_show_lbl["text"]="password : "+self.__password
        captcha_show_lbl["text"]="captcha : "+self.captcha
        

        
user=user_db()

def update():
    global user
    user.username=name_input.get()
    user.password=pass_input.get()
    user.captcha=captcha_input.get()
    print("details updated")

        


btn_update=Button(root,text="update login profile",command=update)
btn_update.place(relx=0.2,rely=0.7,anchor=CENTER)

btn_show=Button(root,text="show profile",command=user.show)
btn_show.place(relx=0.4,rely=0.7,anchor=CENTER)

root.mainloop()

