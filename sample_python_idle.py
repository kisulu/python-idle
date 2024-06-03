from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os

root = Tk()
root.title("Pythin IDLE")
root.geometry("1280x720+150+80")
root.config(bg="#323846")

file_path=''

def set_file_path(path):
    global file_path
    file_path = path
    
def open_file():
    path= askopenfilename(filetypes=[('Python files', '*.py')])
    with open(path, 'r') as file:
        code=file.read()
        code_input.delete('1.0',END)
        code_input.insert('1.0',code)
        set_file_path(path)
        
def save():
    if file_path=='':
        path = asksaveasfilename(filetypes=[('Python files', '*.py')])
    else:
        path=file_path
    with open(path, 'w') as file:
        code = code_input.get('1.0',END)
        file.write(code)
        set_file_path(path)
        
def run():
    if file_path == "":
        messagebox.showerror("Python IDLE", "Save Your Code")
        return
    command =  f'pythin {file_path}'
    process = subprocess.Popen(command,stdout=subprocess.PIPE, sterr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)


# icon
image_icon = PhotoImage(file="pyicon.png")
root.iconphoto(False, image_icon)

# code input

code_input = Text(root, font="consolas 18")
code_input.place(x=180, y=0, width=680, height=720)

# code output
code_output = Text(root, font="consolas 15", bg="#323846", fg="lightgreen")
code_output.place(x=860, y=0, width=420, height=720)

# buttons
Open=PhotoImage(file="open.png")
Save=PhotoImage(file="save.png")
Run=PhotoImage(file="run.png")

Button(root, image=Open, bg="#323846",bd=0, command=open_file).place(x=30, y=30)
Button(root, image=Save, bg="#323846",bd=0, command=save).place(x=30, y=145)
Button(root, image=Run, bg="#323846",bd=0, command=run).place(x=30, y=260)

root.mainloop()