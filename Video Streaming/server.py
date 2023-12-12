import socket
import cv2
import pickle
import struct
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import Font



root=Tk()
root.geometry("925x500+300+200")
root.resizable(False, False)
root.config(bg="#fff")

def ch():
    username=tx.get()
    password=tx1.get()
    if username == "admin" and password == "1234":
        # Set the desired IP address here
        host_ip = "10.5.254.157"

        port = 9999
        socket_address = (host_ip, port)

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(socket_address)
        server_socket.listen(5)
        print("LISTENING AT:", socket_address)

        while True:
            client_socket, addr = server_socket.accept()
            print('GOT CONNECTION FROM:', addr)
            if client_socket:
                vid = cv2.VideoCapture(0)

                while vid.isOpened():
                    img, frame = vid.read()
                    a = pickle.dumps(frame)
                    message = struct.pack("Q", len(a)) + a
                    client_socket.sendall(message)

                    cv2.imshow('TRANSMITTING VIDEO', frame)
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        client_socket.close()
        
        
        
        
    else:
        messagebox.showerror("error","wrong Username or password")
        
        
        



root.title("SERVER LOGIN")
root.iconbitmap("favicon.ico")

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

tx1=Entry(frame,border=0,width=25,show="*",font=('Microsoft YaHei UI Light',11))
tx1.place(x=30,y=150)
tx1.insert(0,"Password")
tx1.bind("<FocusIn>", on_enter)
tx1.bind("<FocusOut>", on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
    
    
    
myfont=Font(family="times",size=20,weight="bold")

mylabel= Label(root,text="Server Streaming", font=myfont,fg="steelblue1")
mylabel.pack()


bu=Button(frame,text="LogIn",pady=7,width=39,bg="#57a1f8",fg="white",border=0, activebackground="#57a1f8",activeforeground="white" ,command=ch)
bu.place(x=35,y=204)


root.mainloop()

    


