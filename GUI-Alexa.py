import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import datetime
import time
import pyttsx3
import pywhatkit
import pyautogui
import cv2
import boto3

def open_notepad():
    os.system("notepad")
    print("Done")

def open_chrome():
    os.system("chrome")
    print("Done")

def search_on_youtube():
    song=input("Enter song name:")
#     song = text.replace('song', '')
    pywhatkit.playonyt(song)

def launch_instance():
    count=int(input("How many instance you want to launch:"))
    myec2=boto3.client('ec2')
    myec2.run_instances(
        ImageId='ami-0ded8326293d3201b',
        InstanceType='t2.micro',
        MaxCount=count,
        MinCount=1
)

def say_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    engine = pyttsx3.init()
    engine.say('Current time is ' + current_time)
    engine.runAndWait()

def camera_on():
    os.system("start microsoft.windows.camera:")

def turn_off_pc():
    os.system("shutdown -s")

def search_on_spotify():
    os.system("spotify")
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('ya habibi', interval=0.1)
    for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
        time.sleep(2)
        pyautogui.press(key)

def whatsapp_now():
    engine = pyttsx3.init()
    engine.say("Tell me phone No")
    engine.runAndWait()
    number = input("Number please:")
    engine.say("Write your Message here:")
    engine.runAndWait()
    message = input("Message:")
    pywhatkit.sendwhatmsg_instantly(number, message)
    engine.say("Done")
    engine.runAndWait()

def make_folder():
    folder_name = input("Enter folder name: ")
    os.mkdir(folder_name)

def remove_folder():
    folder_name = input("Enter folder name to remove: ")
    os.rmdir(folder_name)

def video():
    cap = cv2.VideoCapture(0)
    status, photo = cap.read()
    while True:
        status, photo = cap.read()
        cv2.imshow("Hi", photo)
        if cv2.waitKey(4) == 13:
            break
    cv2.destroyAllWindows()

def grey_video():
    cap = cv2.VideoCapture(0)
    status, photo = cap.read()
    while True:
        status, photo = cap.read()
        my_grey_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Hi", my_grey_photo)
        if cv2.waitKey(4) == 13:
            break
    cv2.destroyAllWindows()

def click_pic():
    cap = cv2.VideoCapture(0)
    status, photo = cap.read()
    cv2.imshow("Capture", photo)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    

def exit_from_app():
    root.destroy()
    

# Create the tkinter GUI
root = tk.Tk()
root.title("Menu-Driven App")


def create_option_button(text, command):
    button_width = 20  # Set the desired width for the buttons
    button_height = 1  # Set the desired height for the buttons
    pady = 5
    button = tk.Button(root, text=text, font=("Helvetica", 12), command=command, bg="white", width=button_width, height=button_height)
    button.pack(pady=pady)

# Create buttons for each option
create_option_button("Open Notepad", open_notepad)
create_option_button("Open Chrome", open_chrome)
create_option_button("Open YouTube", search_on_youtube)
create_option_button("Launch EC2 Instance", launch_instance)
create_option_button("Time now", say_time)
create_option_button("Open Camera", camera_on)
create_option_button("Shutdown", turn_off_pc)
create_option_button("Open Spotify", search_on_spotify)
create_option_button("WhatsApp", whatsapp_now)
create_option_button("Make Folder", make_folder)
create_option_button("Remove Folder", remove_folder)
create_option_button("Colorful Video", video)
create_option_button("Grey Video", grey_video)
create_option_button("Click Image", click_pic)
create_option_button("Exit", exit_from_app)



# Add buttons for the rest of the options...

# Create a menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# Set the background color to black
root.configure(bg="light blue")

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Exit", command=root.quit)

# Center the window on the screen
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

root.mainloop()
    