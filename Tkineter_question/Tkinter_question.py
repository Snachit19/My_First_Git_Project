import tkinter as tk
from tkcalendar import DateEntry
import tkinter.font as tkfont
from sqlite_in_tkinter import insert_data
application = tk.Tk()
application.title("Records of students")
application.geometry("1425x250")
font_obj = tkfont.Font(size=24)
add_student_label = tk.Label(application,text="Add new record:",font=font_obj)
add_student_label.grid(column=0,row=0)
add_student_name = tk.Entry()
add_name_label = tk.Label(application,text="Name:")
add_name_label.grid(row=1,column=0)
add_student_name.grid(row=1,column=1)
gender_label = tk.Label(application,text="Gender:")
gender_var = tk.StringVar()
gender_button_male = tk.Radiobutton(application,text="Male",value="Male",variable=gender_var)
gender_button_female = tk.Radiobutton(application,text="Female",value="Female",variable=gender_var)
gender_label.grid(row=1,column=2)
gender_button_male.grid(row=1,column=3)
gender_button_female.grid(row=1,column=4)
address_label = tk.Label(application,text="Address:")
address = tk.Entry()
address_label.grid(row=1,column=5)
address.grid(row=1,column=6)
phone_num = tk.Entry()
phone_num_label = tk.Label(application,text="Phone-number:")
phone_num_label.grid(row=1,column=7)
phone_num.grid(row=1,column=8)
grade_label = tk.Label(application,text="Grade of student:")
grade_label.grid(row=3,column=0)
grade_list = ["Grade-1", "Grade-2", "Grade-3", "Grade-4", "Grade-5",\
              "Grade-6", "Grade-7", "Grade-8", "Grade-9", "Grade-10"]
grade_value = tk.StringVar(application)
grade_value.set("Select the grade")
grade_menu = tk.OptionMenu(application,grade_value,*grade_list)
grade_menu.grid(row=3,column=1,columnspan=2)
date_of_birth_label = tk.Label(application,text="Date of birth:")
date_of_birth_label.grid(row=3,column=3)
birthday_date_input = DateEntry(application,selectmode="day",\
                                date_pattern="yyyy-mm-dd",width=15)
birthday_date_input.grid(row=3,column=4)
math_marks_label = tk.Label(application,text="Math marks:")
math_marks_label.grid(row=3,column=5)
math_marks_input = tk.Entry()
math_marks_input.grid(row=3,column=6)
science_marks_label = tk.Label(application,text="Science marks:")
science_marks_label.grid(row=3,column=7)
science_marks_input = tk.Entry()
science_marks_input.grid(row=3,column=8)
english_marks_label = tk.Label(application,text="English marks:")
english_marks_label.grid(row=4,column=0)
english_marks_input = tk.Entry()
english_marks_input.grid(row=4,column=1)
computer_marks_label = tk.Label(application,text="Computer marks:")
computer_marks_label.grid(row=4,column=2)
computer_marks_input = tk.Entry()
computer_marks_input.grid(row=4,column=3)
def get_student_info():
    name = add_student_name.get()
    if gender_var.get() == "Male":
        gender = "Male"
    elif gender_var.get() == "Female":
        gender = "Female"
    address_got = address.get()
    phone_number = int(phone_num.get())
    grade = grade_value.get()
    birthday_date = birthday_date_input.get()
    math_marks = int(math_marks_input.get())
    science_marks = int(science_marks_input.get())
    english_marks = int(english_marks_input.get())
    computer_marks = int(computer_marks_input.get())
    average = (math_marks + science_marks + english_marks + computer_marks) / 4
    input_database = (name, gender, address_got, phone_number,\
                      grade, birthday_date, math_marks, science_marks,\
                          english_marks, computer_marks, average)
    print(input_database)
    insert_data(input_database)
submit_button = tk.Button(application,text="Submit information",command=get_student_info)
submit_button.grid(row=5,column=1)
application.mainloop()