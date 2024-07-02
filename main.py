
# Online Python - IDE, Editor, Compiler, Interpreter
import cv2
from pyzbar import pyzbar
import os
import tkinter as tk
from tkinter import Message ,Text
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter import *
##from PIL import Image, ImageTk
from PIL import Image
from datetime import *
import time
date=datetime.now().strftime("%m-%d %H:%M")
val1=str(date)
##import serial
##ser = serial.Serial('COM8', 9600)
#import serial
def ped():
video_src = 'pedestrians.avi'
cap = cv2.VideoCapture(video_src)
bike_cascade = cv2.CascadeClassifier('pedestrian.xml')
while True:
ret, img = cap.read()
if (type(img) == type(None)):

break
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bike = bike_cascade.detectMultiScale(gray,1.3,2)

for(a,b,c,d) in bike:
cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,210),4)
cv2.imshow('video', img)
if cv2.waitKey(33) == 27:
break
cv2.destroyAllWindows()
def auto():
global image,image1,image2,image3
cascade_src = 'cars.xml'
video_src = 'dataset/video3.mp4'
#video_src = 'dataset/Cars On The Road.mp4'
#ser = serial.Serial('COM6', 9600)
cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
num = 0
while num<2:
ret, img = cap.read()
if (type(img) == type(None)):
break
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

for (x,y,w,h) in cars:
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#%cv2.imshow('video', img)
cv2.imwrite('img2.jpg',img)
cv2.imshow('img2.jpg',img)
num = num+1
image = cv2.imread("img2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
car_cascade = cv2.CascadeClassifier(cascade_src)
car = car_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3,minSize=(30,
30))
a=(str(len(cars)))
print((a))
video_src = 'dataset/training_video.mp4'
#ser = serial.Serial('COM6', 9600)
cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
num = 0
while num<2:
ret, img = cap.read()
if (type(img) == type(None)):
break
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.1, 1)
for (x,y,w,h) in cars:

cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#cv2.imshow('video', img)
cv2.imwrite('img3.jpg',img)
cv2.imshow('img3.jpg',img)
num = num+1
image1 = cv2.imread("img3.jpg")
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
car_cascade = cv2.CascadeClassifier(cascade_src)
car = car_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3,minSize=(30,
30))
b=(str(len(cars)))
print((b))
video_src = 'dataset/video4.mp4'
#video_src = 'dataset/training_video.mp4'
#ser = serial.Serial('COM6', 9600)
cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
num = 0
while num<2:
ret, img = cap.read()
if (type(img) == type(None)):
break
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.1, 1)
for (x,y,w,h) in cars:

cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#cv2.imshow('video', img)
cv2.imwrite('img4.jpg',img)
cv2.imshow('img4.jpg',img)
num = num+1
image2 = cv2.imread("img4.jpg")
gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
car_cascade = cv2.CascadeClassifier(cascade_src)
car = car_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3,minSize=(30,
30))
c=(str(len(cars)))
print((c))
a1=int(a)
b1=int(b)
c1=int(c)
if a1>b1 and a1>c1 or a1==b1 or a1==c1:
print("a go")
if b1>c1 or b1==c1:
print("b go")
print("c go")
else:
print("c go")
print("b go")
elif b1>a1 and b1>c1 or b1==c1:
print("b go")

if a1>c1 or a1==c1:
print("a go")
print("c go")
else:
print("c go")
print("a go")
if c1>b1 and c1>a1:
print("c go")
if b1>a1 or b1==a1:
print("b go")
print("a go")
else:
print("a go")
print("b go")
cv2.destroyAllWindows()
def emer():
window = tk.Tk()
window.title("ambulance_detection")
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
message = tk.Label(window, text="TRAFFIC CONTROL SYSTEM FOR EMERGENCY
VEHICLES" ,bg="white" ,fg="red" ,width=60 ,height=4,font=('times', 30, 'italic bold
underline'))
message.place(x=100, y=5)

def videocapture():
global user
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
while True:
_, frame = cap.read()
decodedObjects = pyzbar.decode(frame)
for obj in decodedObjects:
user=str(obj.data)
print(user)
## cv2.putText(frame, str(obj.data), (50, 50), font, 2,
##
## (0, 0, 255), 3)
cv2.imshow("AMI IDentifier ", frame)
if cv2.waitKey(1) & 0xFF == ord('x'):
print(" closing ...OK")
break
## o="INSERT INTO `vehicle qrs`(`decodeddata`, `time`) VALUES (%s,%s)"
## attend=(user,val1)
## mycursor.execute(o,attend)
## con.commit()
lab1=tk.Label(window,text="Ambulance detected" ,bg="red",font=('times', 15, ' bold '))
lab1.place(x=100, y=200)
cap.release()
cv2.destroyAllWindows()
def qrcheck():
global user1
cap = cv2.imread("qr.png")
font = cv2.FONT_HERSHEY_PLAIN
decodedObjects = pyzbar.decode(cap)
for obj in decodedObjects:
user1=str(obj.data)
print(user1)
lab2=tk.Label(window,text="Checking progressing....... click QRCompare"
,bg="yellow",font=('times', 15, ' bold '))
lab2.place(x=100, y=300)
cv2.destroyAllWindows()
def qrcompare():
if user==user1:
lab=tk.Label(window,text="buzzer on....... traffic signal changed"
,bg="green",font=('times', 15, ' bold '))
lab.place(x=100, y=400)
else:
lab=tk.Label(window,text="oh..... its not an emergency vehicle"
,bg="green",font=('times', 15, ' bold '))
lab.place(x=100, y=400)
videocapture= tk.Button(window, text="Ambulance Detection", command=videocapture
,fg="red" ,bg="black" ,width=20 ,height=3, activebackground = "Red" ,font=('times', 15, '
bold '))
videocapture.place(x=100, y=500)

qrcheck = tk.Button(window, text="QR code Checking ", command=qrcheck
,fg="yellow" ,bg="black" ,width=20 ,height=3, activebackground = "Red" ,font=('times',
15, ' bold '))
qrcheck.place(x=400, y=500)
qrcompare = tk.Button(window, text="QRCompare", command=qrcompare ,fg="green"
,bg="black" ,width=20 ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
qrcompare.place(x=700, y=500)
quitWindow = tk.Button(window, text="Quit", command=window.destroy ,fg="white"
,bg="black" ,width=20 ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1000, y=500)
window.mainloop()
def main_account():
global main_screen0
main_screen0 = Tk()
main_screen0.geometry("500x500")
main_screen0.title("college erp")
main_screen0.configure(bg="blue")
Label(text="AUTOMATIC TRAFFIC CONTROL SYSTEM", bg="blue", width="300",
height="2", font=("Calibri bold", 17)).pack()
Label(text="",bg="blue").pack()
## image = Image.open('traffic.png')
## photo_image = ImageTk.PhotoImage(image)
## Label(image = photo_image,width='210',height='210').pack()
Label(text="",bg="blue").pack()
Button(text="TRAFFIC SYSTEM", height="2", width="30", command = auto).pack()


Automatic Traffic Control Signal System Page 39
Label(text="",bg="blue").pack()
Button(text="PEDESTRIAN DETECTION", height="2", width="30", command =
ped).pack()
Label(text="",bg="blue").pack()
Button(text="EMERGENCY VEHICLE", height="2", width="30", command =
emer).pack()
Label(text="",bg="blue").pack()
Button(text="QUIT", height="2", width="30",command=main_screen0.destroy).pack()
main_screen0.mainloop()
main_account()