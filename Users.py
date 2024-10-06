 import pandas as pd
 import numpy as np
 from tkinter import messagebox
 from tkinter import *
 from tkinter.filedialog import askopenfilename
 from tkinter import simpledialog
 import tkinter
 from tkinter import filedialog
 import os
 import socket
 import cv2
 root = tkinter.Tk()
 60
root.title("User Personalized Data Treatment Screen")
 root.geometry("800x700")
 global filename
 def upload():
 text.delete('1.0', END)
 global filename
 filename = filedialog.askopenfilename(initialdir="data")
 pathlabel.config(text=filename)
 host = socket.gethostname() # as both code is running on same pc
 port = 5000 # socket server port number
 filedata = ""
 diet = ""
 with open("img/plan.txt", "r", errors='ignore') as file:
 for line in file:
 diet+=line+" "
 with open(filename, "r", errors='ignore') as file:
 for line in file:
 line = line.strip('\n')
 filedata+=line+" "
 file = filedata.split(" ")
 length = len(file)
 print(length)
 i = 0
 j = 0
 while i < (length-1):
 client_socket = socket.socket() # instantiate
 client_socket.connect((host, port)) # connect to the server
 message = str(file[i])
 61
 text.insert(END,"User Sense Data : "+message+"\n")
client_socket.send(message.encode()) # send message
 data = client_socket.recv(1024).decode() # receive response
 if str(data) == '1':
 print("Abnormal Values. Disease predicted as type 2
 diabetes\n")
 text.insert(END,"Abnormal Values. Predicted values :
 "+str(data)+" Disease predicted as type 2 diabetes\n")
 else:
 text.insert(END,"Normal Values. Predicted values :
 "+str(data)+" No disease predicted\n")
 root.update_idletasks()
 client_socket.close()
 i = i + 1
 if j == 0 and str(data) == '1':
 img = cv2.imread("img/1.jpg");
 cv2.imshow("Diet Plan Img",img)
 text1.insert(END,"Diet Plan Details\n\n"+diet)
 j = 1
 font = ('times', 18, 'bold')
 title = Label(root, text='5G-Smart Diabetes: Toward Personalized
 Diabetes Diagnosis with Healthcare Big Data Clouds')
 title.config(bg='wheat', fg='blue')
 title.config(font=font)
 title.config(height=3, width=80)
 title.place(x=5,y=5)
 font1 = ('times', 14, 'bold')
 upload = Button(root, text="Upload Files", command=upload)
 upload.place(x=50,y=100)
 upload.config(font=font1)
 62
pathlabel = Label(root)
 pathlabel.config(bg='blue', fg='white')
 pathlabel.config(font=font1)
 pathlabel.place(x=300,y=100)
 font1 = ('times', 12, 'bold')
 text=Text(root,height=10,width=120)
 scroll=Scrollbar(text)
 text.configure(yscrollcommand=scroll.set)
 text.place(x=50,y=150)
 text.config(font=font1)
 text1=Text(root,height=15,width=120)
 scroll1=Scrollbar(text)
 text1.configure(yscrollcommand=scroll1.set)
 text1.place(x=50,y=350)
 text1.config(font=font1)
 root.mainloop()
