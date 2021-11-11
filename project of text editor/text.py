# here first we will import all the necessary modules and here we imported tkinter as tk
import tkinter as tk
#this filedialog is a part of tkinter module used to open a file or to save 
from tkinter.filedialog import askopenfilename, asksaveasfilename
#new window by tkinter 
windows=tk.Tk()
#setting title of the window
windows.title("Simple Text Editor")
#setting the icon of the title bar but here makesure to give file adress of image present in your computer 
photo = tk.PhotoImage(file = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\achievements\\project of text editor\\Simple Text  Editor.png")
windows.iconphoto(False, photo)
#its to conifgure and make window responive
windows.rowconfigure(0,weight=1,minsize=600)
windows.columnconfigure(1,weight=1,minsize=600)

#function called when open button is clicked or b1 
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:#its a condition when no path came when clicked 
        return
    t1.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        t1.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


#function is called when b2 is called its for save
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = t1.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


#created all the required widgets in the program     
f1=tk.Frame(windows)
b1=tk.Button(master=f1,text="OPEN",command=open_file)
b1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
b2=tk.Button(master=f1,text="SAVE AS...",command=save_file)
b2.grid(row=1, column=0, sticky="ew", padx=5)
t1=tk.Text(windows)
f1.grid(row=0, column=0, sticky="ns")
t1.grid(row=0, column=1, sticky="nsew")

#at the end for event handling and all 
windows.mainloop()
