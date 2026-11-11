# Workbook to create , load_workbook to read
from openpyxl import Workbook , load_workbook
import smtplib
from email.message import EmailMessage


#initial Workbook for excel file , and read the excel 
workbook_initial = Workbook()
active_sheet = workbook_initial.active


#excel data
headers = ["rollno", "mailid" ,"CI", "Python", "DS" ]
students = [
      [1 , "gaber@tubahealth.com" , 0 , 1 , 2],
      [2 , "Frog@tubahealth.com" , 2 , 1 , 3],
      [3 , "mahmoud@tubahealth.com" , 3 , 0 , 1] 
]

#email data
sender_email = "m.gaber@tubahealth.com"
app_password = "ukdi anug gyxc cmvt"
receiver_email = "mahmoud.gr231@gmail.com"
file_path = "/Users/mahmoudgaber/python-tasks/Students Attendance.xlsx"


#setup mail values 
msg = EmailMessage()
msg["Subject"] = "Report Attached"
msg["From"] = sender_email
msg["To"] = receiver_email

#appened the static data for the excel
active_sheet.append(headers)


#create excel file 
def create_excel():
      #title for the file 
      active_sheet.title = "Attendance Excel Sheet"
      #append students
      for student in students:
            active_sheet.append(student)
      #save file as it is 
      workbook_initial.save("Students Attendance.xlsx") 


# take input from staff and make sure that it's match my length 
def choose_subject_and_student():
      # get the number of subject by ignore the static 2 columns 
      subject_count = len(headers) - 2
      student_count = len(students) 
      global subject_number 
      global student_roll_number 

      # take the subject number and make sure that he enter the right number 
      subject_number = int(input("\n C1 = 1 \n Python = 2 \n DS = 3 \n Please Enter Subject Number :  "))
      while subject_number < 1 or subject_number > subject_count:
            print(f"Invalid input! Please enter a number between 1 and {subject_count}.")
            subject_number = int(input("Please Enter Subject Number: "))

      #take the number of absent student 
      student_roll_number = int(input("Please Enter Student Roll Number: "))
      while student_roll_number < 1 or student_roll_number > student_count:
            print(f"Invalid input! Please enter a number between 1 and {student_count}.")
            student_roll_number = int(input("Please Enter Student Roll Number: "))
      update_absence_record()

#read exist excel file and edit on it 
def update_absence_record():
      global student_roll_number 
      global subject_number 
      #load the excel file 
      workbook_initial = load_workbook("Students Attendance.xlsx")
      attendance_sheet = workbook_initial.active
      # take target subject and student rollno and add to them the static value that get me the place of the data in the excel sheet
      target_cell = attendance_sheet.cell(row=student_roll_number + 1, column=subject_number+2)
      # add the value to the old data and then check it 
      target_cell.value = target_cell.value + 1 if target_cell.value < 3 else  target_cell.value
      workbook_initial.save("Students Attendance.xlsx") 
      repeat_choice = input(" There is Another Process or you have end your job ? (y/n)")

      if repeat_choice.lower() == 'y':
            choose_subject_and_student()
      elif repeat_choice.lower() == 'n':
            if target_cell.value == 2:
                  send_mail("Warning please care for you attendance")
            elif target_cell.value == 3:
                  send_mail("you have reach the limit for absent")


def send_mail(message_body):
      msg.set_content(message_body)
      with open(file_path, "rb") as file:
        msg.add_attachment(
            file.read(),
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename="Students Attendance.xlsx",
        )

      with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
      

create_excel()
choose_subject_and_student()

# naming convention -- done
# global, using import for method in the class
# 2. oop
# 3. use pydantic to validate user input
# 4. 