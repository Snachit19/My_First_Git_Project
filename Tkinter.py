import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Tkinter Window")
root.geometry("600x600")

#adding label
label = tk.Label(root,text="Hello I am Tanmay!")
label.pack()

#adding button
def click_button():
    print("Button clicked")
button = tk.Button(root,\
                   text='Submit',\
                    command=click_button)
button.pack()

#adding input
Input = tk.Entry(root)
Input.pack()

#adding Text area
text_area = tk.Text(root,height=5,width=50)
text_area.pack()

#adding frame
frame = tk.Frame(root,bg="blue")

#adding check box 
check = tk.IntVar()
check_button = tk.Checkbutton(frame,\
                              text="Check me",\
                                variable=check)
check_2 = tk.IntVar()
check_button_2 = tk.Checkbutton(frame,\
                                text="Check me 2",\
                                    variable=check_2)
check_button.pack()
check_button_2.pack()

#adding radio box
radio_var = tk.StringVar()
radio_button = tk.Radiobutton(frame,\
                              text="Male",\
                                value="M")
radio_var_2 = tk.StringVar()
radio_button_2 = tk.Radiobutton(frame,\
                                text="Female",\
                                    value="F")
radio_button.pack()
radio_button_2.pack()

frame.pack()

#adding menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="Menu",menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Exit",command=root.quit)

#treeview 
tree = ttk.Treeview(root)
tree["columns"] = ("Name","Age")
tree.column("#0",width=150)
tree.column("Name",width=100)
tree.column("Age",width=100)
tree.heading("#0",text="ID")
tree.heading("Name",text="Name")
tree.heading("Age",text="Age")
tree.insert("",0,text="1",values=("xx","yy"))
tree.pack()

root.mainloop()#This fuction is used so that application not closed automatically