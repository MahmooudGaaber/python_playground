# Workbook to create , load_workbook to read
from openpyxl import Workbook , load_workbook
from pathlib import Path
import smtplib
from email.message import EmailMessage
from take_absent_model import TakeAbsentData

#initial Workbook for excel file , and read the excel 
staff_workbook = Workbook()
staff_sheet = staff_workbook.active

#initial Workbook for excel file , and read the excel 
student_workbook = Workbook()
student_sheet = student_workbook.active

#excel data
headers = ["rollno", "mailid" ,"CI", "Python", "DS" ]
students = [
      [1 , "gaber@tubahealth.com" , 0 , 1 , 2],
      [2 , "Frog@tubahealth.com" , 2 , 1 , 3],
      [3 , "mahmoud@tubahealth.com" , 3 , 0 , 1] 
]
take_absent = TakeAbsentData( len(students) ,len(headers) - 2 )

#email data
sender_email = "m.gaber@tubahealth.com"
app_password = "ukdi anug gyxc cmvt"
receiver_email = "mahmoud.gr231@gmail.com"


#setup mail values 
msg = EmailMessage()
msg["Subject"] = "Report Attached"
msg["From"] = sender_email
msg["To"] = receiver_email


#appened the static data for the excel
staff_sheet.append(headers)

#create excel file 
def create_excel_for_staff():
      #title for the file 
      staff_sheet.title = "Attendance Excel Sheet"
      #append students
      for student in students:
            staff_sheet.append(student)
      #save file as it is 
      staff_workbook.save("Students Attendance.xlsx") 

def create_excel_for_student(
      subject ,
      student_data
):
      #title for the file 
      student_sheet.title = f"{subject} Attendance"
      student_sheet.append(headers)
      #append students
      student_sheet.append(student_data)
      #save file as it is 
      student_workbook.save(f"{subject} Attendance.xlsx") 
      


# take input from staff and make sure that it's match my length 
def choose_subject_and_student():
      # take the subject number and make sure that he enter the right number 
      subject_number = input("\n C1 = 1 \n Python = 2 \n DS = 3 \n Please Enter Subject Number :  ")
      take_absent.set_subject(subject_number)
      #take the number of absent student 
      student_roll_number = input(" Please Enter Student Roll Number: ")
      take_absent.set_student(student_roll_number)
      update_absence_record()

#read exist excel file and edit on it 
def update_absence_record():
      #load the excel file 
      staff_workbook = load_workbook("Students Attendance.xlsx")
      staff_sheet = staff_workbook.active
      # take target subject and student rollno and add to them the static value that get me the place of the data in the excel sheet
      target_cell = staff_sheet.cell(row=take_absent.student + 1, column=take_absent.subject+2)
      # add the value to the old data and then check it 
      target_cell.value = target_cell.value + 1 if target_cell.value < 3 else  target_cell.value
      staff_workbook.save("Students Attendance.xlsx")
      updated_student = [cell.value for cell in staff_sheet[take_absent.student+1]]
      create_excel_for_student(headers[take_absent.subject+1] , updated_student)
      if target_cell.value == 2:
                  send_mail("Warning please care for you attendance" ,f"{headers[take_absent.subject+1]} Attendance" )
      elif target_cell.value == 3:
                  send_mail("you have reach the limit for absent",f"{headers[take_absent.subject+1]} Attendance")
      
      repeat_operation(f"{headers[take_absent.subject+1]} Attendance")


def send_mail(message_body , file_name):
      msg.set_content(message_body)
      with open(f"/Users/mahmoudgaber/python-tasks/{file_name}.xlsx", "rb") as file:
        msg.add_attachment(
            file.read(),
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=f"{file_name}.xlsx",
        )
      with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
      msg.clear_content()
      
def repeat_operation(file_name):
      repeat_choice = input(" There is Another Process or you have end your job ? (y for repeat)")
      if repeat_choice.lower() == 'y':
            student_sheet.delete_rows(1, student_sheet.max_row)
            choose_subject_and_student()
      else:
            clear_project(file_name)
            print("Thanks For Your Effort")


def clear_project(file_name):
      student_workbook.close()
      file_path = Path(f"{file_name}.xlsx")
      file_path.unlink(missing_ok=True)
      msg.clear_content()
      

create_excel_for_staff()
choose_subject_and_student()



# naming convention -- done
# global -- done
# using import for method in the class -- done
# 2. oop
# 3. use pydantic to validate user input
# 4. 

