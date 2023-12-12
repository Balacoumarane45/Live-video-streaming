from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import Font

#import MySQLDb as sql
#from PIL import ImageTk


root=Tk()
root.geometry("925x500+300+200")
root.resizable(False, False)
root.config(bg="#fff")

def log():
    root1=Toplevel(root)
    root1.geometry("1080x720")
    root1.resizable(False, False)
    root1.config(bg="#fff")
    
    myfont1=Font(family="Microsoft YaHei UI Light",size=13,weight="bold")
    
    main_frame=Frame(root1,bg="white")
    main_frame.pack(pady=5)
    main_frame.pack_propagate(False)
    main_frame.configure(width=1080,height=50)
    img2 = PhotoImage(file = "logo (2).png")
    label3 = Label( main_frame, image = img2)
    label3.place(x = 995, y = -5)
    
    
        
    
    def switch(in_lb,page):
        
        for child in main_frame.winfo_children():
            if isinstance(child,Label):
                child['bg']="SystemButtonFace"
                
        in_lb['bg']="#51a1f8"
        
        for fm in op_frame.winfo_children():
            fm.destroy()
            root1.update()
        
        page()
    
    bt1=Button(main_frame,text="Home",font=myfont1,bd=0,bg="white",fg="#51a1f8",command=lambda:switch(in_lb=bt1_lb,page=home))
    bt1.place(x=0,y=0)
    bt1_lb=Label(main_frame,bg="#51a1f8")
    bt1_lb.place(x=0,y=35,width=80,height=2)
    
    bt2=Button(main_frame,text="NetBanking",font=myfont1,bd=0,bg="white",fg="#51a1f8",command=lambda:switch(in_lb=bt2_lb,page=net))
    bt2.place(x=100,y=0)
    bt2_lb=Label(main_frame)
    bt2_lb.place(x=100,y=35,width=120,height=2)
    
    bt3=Button(main_frame,text="page3",font=myfont1,bd=0,bg="white",fg="#51a1f8",command=lambda:switch(in_lb=bt3_lb,page=pag3))
    bt3.place(x=250,y=0)
    bt3_lb=Label(main_frame)
    bt3_lb.place(x=250,y=35,width=80,height=2)
    
    bt4=Button(main_frame,text="page4",font=myfont1,bd=0,bg="white",fg="#51a1f8",command=lambda:switch(in_lb=bt4_lb))
    bt4.place(x=400,y=0)
    bt4_lb=Label(main_frame)
    bt4_lb.place(x=400,y=35,width=80,height=2)
    
    def home():
        home_fm=Frame(op_frame)
        home_fm.pack(fill=BOTH,expand=True)
        home_lb=Label(home_fm,text="Home Page",font=myfont1,fg="#51a1f8")
        home_lb.pack(pady=80)
        """img2 = PhotoImage(file = "redwhite.png")
        home_lb1 = Label( home_fm, image = img2)
        home_lb1.place(x = 0, y = 0)"""
        #home_fm1=Frame(home_fm,width=300,height=100)
        #home_fm1.pack()
        

    def net():
        net_fm=Frame(op_frame)
        net_fm.pack(fill=BOTH,expand=True)
        net_lb=Label(net_fm,text="NetBanking",font=myfont1,fg="#51a1f8")
        net_lb.pack(pady=50)
        
        net_fm1=Frame(net_fm,bg="white",width=720,height=420)
        net_fm1.place(x=170,y=80)
        
        
        
        net_tx=Entry(net_fm1,border=0,width=25,font=('Microsoft YaHei UI Light',11))
        net_tx.place(x=100,y=160)
        Frame(net_fm1,width=230,height=2,bg="black").place(x=95,y=180)
        
        net_lb1=Label(net_fm1,text="Account Category",font=myfont1,fg="#51a1f8",bg="white")
        net_lb1.place(x=100,y=70)
        
        
        def on_enter1(e):
            
            net_tx.delete(0,"end")
        def on_leave1(e):
            if name==" ":
                net_tx.insert(0,"Password")
                
                
        
        
        def combobox(event):
            data=cb.get()
            
        
        cb=ttk.Combobox(net_fm1,width=30,height=20,state="readonly")
        cb["values"]=("SWISS Bank","Other Bank")
        cb.current(0)
        cb.bind("<<ComboboxSelected>>",combobox)
        cb.place(x=100,y=100)
        
        net_lb2=Label(net_fm1,text="TO",font=myfont1,fg="#51a1f8",bg="white")
        net_lb2.place(x=100,y=130)
        net_tx.insert(0,"Enter Account Number")
        net_tx.bind("<FocusIn>", on_enter1)
        net_tx.bind("<FocusOut>", on_leave1)
        
        net_lb3=Label(net_fm1,text="Account Type",font=myfont1,fg="#51a1f8",bg="white")
        net_lb3.place(x=100,y=190)
        cb1=ttk.Combobox(net_fm1,width=30,height=23,state="readonly")
        cb1["values"]=("Savings Account","Current Account")
        cb1.current(0)
        cb1.bind("<<ComboboxSelected>>",combobox)
        cb1.place(x=100,y=220)
        
        net_lb4=Label(net_fm1,text="Select transfer mode",font=myfont1,fg="#51a1f8",bg="white")
        net_lb4.place(x=100,y=245)
        cb2=ttk.Combobox(net_fm1,width=30,height=23,state="readonly")
        cb2["values"]=("NEFT","IMPS","IMPS-through MMID")
        cb2.current(0)
        cb2.bind("<<ComboboxSelected>>",combobox)
        cb2.place(x=100,y=275)
        
        
        
        net_bt=Button(net_fm1,text="Continue",font=myfont1,bd=0,bg="white",fg="#51a1f8",activebackground="white",activeforeground="#51a1f8")
        net_bt.place(x=310,y=360)
        
        img2 = PhotoImage(file = "UBS-Logo.png")
        home_lb1 = Label( net_fm1, image = img2)
        home_lb1.place(x = 0, y = 0)
        
        
        
        """net_tx1=Entry(net_fm1,border=0,width=20,font=('Microsoft YaHei UI Light',11))
        net_tx1.place(x=100,y=180)"""
        
        
    def pag3():
        pag3_fm=Frame(op_frame)
        pag3_fm.pack(fill=BOTH,expand=True)
        pag3_lb=Label(pag3_fm,text="page3",font=myfont1,fg="#51a1f8")
        pag3_lb.pack(pady=80)
        
    
    op_frame=Frame(root1,bg="white")
    op_frame.pack(fill=BOTH,expand=True)
    home()
    
    root1.mainloop()
    
    
    
   
    
    
    

   

def ch():
    username=tx.get()
    password=tx1.get()
    if username == "admin" and password == "1234":
        log()
        
        
    else:
        messagebox.showerror("error","wrong Username or password")
        
        
        



root.title("ATM SIMULATOR")
root.iconbitmap("ATM.ico")

img = PhotoImage(file = "BTweeps-Login-Background (1).png")
label1 = Label( root, image = img) 
label1.place(x = 0, y = 0)

img1 = PhotoImage(file = "Login.png")
label2 = Label( root, image = img1) 
label2.place(x = 0, y = 0)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
he=Label(frame,text="Log In",bg="white",fg="#51a1f8",font=("Microsoft YaHei UI Light",23,"bold"))
he.place(x=100,y=5)

def on_enter(e):
    tx.delete(0,"end")
def on_leave(e):
    if name=="":
        tx.insert(0,"Username")
    

tx=Entry(frame,border=0,width=25,font=('Microsoft YaHei UI Light',11))
tx.place(x=30,y=80)
tx.insert(0,"Username")
tx.bind("<FocusIn>", on_enter)
tx.bind("<FocusOut>", on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

def on_enter(e):
    tx1.delete(0,"end")
def on_leave(e):
    if name==" ":
        tx1.insert(0,"Password")

tx1=Entry(frame,border=0,width=25,font=('Microsoft YaHei UI Light',11))
tx1.place(x=30,y=150)
tx1.insert(0,"Password")
tx1.bind("<FocusIn>", on_enter)
tx1.bind("<FocusOut>", on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
    
    
    
myfont=Font(family="times",size=20,weight="bold")

mylabel= Label(root,text="SWISS BANK", font=myfont,fg="steelblue1")
mylabel.pack()







        
bu=Button(frame,text="LogIn",pady=7,width=39,bg="#57a1f8",fg="white",border=0, activebackground="#57a1f8",activeforeground="white" ,command=ch)
bu.place(x=35,y=204)


root.mainloop()
