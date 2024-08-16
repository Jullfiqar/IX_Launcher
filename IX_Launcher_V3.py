import tkinter as tk
from tkinter import filedialog
from tkinter import *
import subprocess

# Set Variable afi_process is None
afi_process = None

# Define a Function Python
def open_file():
    win.openfile = filedialog.askopenfilename(initialdir="/mnt/res/_EXPLOITATION", title="Choose afi Files", filetypes=[("Text Files", "*.txt"), ("Afi Files", ".afi"), ("All Files", "*.*")])
    if win.openfile:
        text_box.delete(1.0, END)
        text_box.insert(END, win.openfile)
        buttonRunAfi.config(state=NORMAL)
    #print("eclrun --gpu ix", win.openfile)

#def run_command():
    #global process
    #process_ping = subprocess.Popen(["ping", "8.8.8.8"])

#def stop_command():
    #global process
    #if process_ping.poll() is not None:
        #process.terminate()

def run_afi():
    global runAfi
    runAfi = subprocess.Popen(["/indo/apps/Linux/ecl/macros/eclrun", "--gpu", "ix", win.openfile])
    
def run_sh():
    global process
    process_ping = subprocess.Popen(["ping", "8.8.8.8"])

def stop_afi():
    global runAfi
    if win.openfile is not None:
        runAfi.kill()
    print("Terminating Process")

def frame_about():
    hide_frame()
    current_status.set("About")
    text.grid(row=0, column=0)


def frame_single():
    current_status.set("Home")
    hide_frame()
    button.grid(row=4, column=1, sticky="w")
    #buttonStop.grid()
    buttonRunAfi.grid(column=1, columnspan=2, row=5, sticky="w")
    buttonRunSh.grid(column=2, columnspan=2, row=5, sticky="w")
    buttonCancelAfi.grid(column=1,row=6, sticky="w")
    statusBar.grid(row=8, columnspan=8, sticky="w"+"e")
    text_box.grid(row=4, column=2)
    rbuttonsingle.grid(row=0, column=1, sticky="w")
    rbuttoncoupling.grid(row=1, column=1, sticky="w")

def hide_frame():
    text.grid_forget()
    button.grid_forget()
    #buttonStop.grid_forget()
    buttonRunAfi.grid_forget()
    buttonRunSh.grid_forget()
    buttonCancelAfi.grid_forget()
    rbuttonsingle.grid_forget()
    rbuttoncoupling.grid_forget()
    text_box.grid_forget()


# Root Box Windows
win = tk.Tk()
win.title("IX - Intersect Linux Launcher")
win.geometry("900x400")

# Configure row and column weight biar Responsive
for i in range(9):
    win.grid_rowconfigure(i, weight=1)

for j in range(9): # Adjust the range according to the number of columns
    win.grid_columnconfigure(j, weight=1)

# Text Box for Open file Variable
text_box = Text(win, bg="white", width=80, height=2, wrap=WORD)


# Create Menu Bar Variable
MenuBar = Menu(win)
win.config(menu=MenuBar)

# Create Menu Items Variable
Home = Menu(MenuBar)
MenuBar.add_cascade(label="Home", menu=Home)
Home.add_command(label="Home", command=frame_single)

About = Menu(MenuBar)
MenuBar.add_cascade(label="About", menu=About)
About.add_command(label="About", command=frame_about)

# Radio Button Variable
rbuttonsingle = Radiobutton(win, text="Running Single Model", value=1)
rbuttoncoupling = Radiobutton(win, text="Running Coupling Model", value=2)


# Status Bar Variable
current_status = StringVar()
statusBar = Label(win, textvariable=current_status, bd=2, relief="sunken", anchor=E)
text = Label(win, text="This tkinter GUI launcher is specifically designed to execute the '.afi intersect' command easily and efficiently. With an intuitive user interface, you can execute the command with just a single click of a button. Enjoy the convenience of running your command without having to remember the syntax or type it manually.\n\nThank you for using my launcher application! - Version : Beta 0.0.3\n\n21,July 2023 - Fadhil Dzulfiqar", wraplength=500, justify="left")

#buttonStop = tk.Button(win, text="Stop Command", command=stop_command)
#buttonStop.pack(side="bottom", anchor="se")

# Button Variable
button = tk.Button(win, text="Open File", command=open_file, width=20, height=2)
buttonRunAfi = tk.Button(win, text="Run Afi (Single Model)", command=run_afi, width=20, height=2, state=DISABLED)
buttonRunSh = tk.Button(win, text="Run Sh (Coupling Model)", command=run_sh, width=20, height=2, state=DISABLED)
buttonCancelAfi = tk.Button(win, text="Terminate Process", command=stop_afi, width=20, height=2)

win.mainloop()
