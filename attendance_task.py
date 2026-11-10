# Workbook to create , load_workbook to read
from openpyxl import Workbook , load_workbook
import smtplib
from email.message import EmailMessage


#initial Workbook for excel file , and read the excel
workBookIntial = Workbook()
activeSheet = workBookIntial.active


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
activeSheet.append(headers)


#create excel file 
def createExcel():
      #title for the file 
      activeSheet.title = "Attendance Excel Sheet"
      #append students
      for student in students:
            activeSheet.append(student)
      #save file as it is 
      workBookIntial.save("Students Attendance.xlsx") 


# take input from staff and make sure that it's match my length 
def makeStaffChooseSubject():
      # get the number of subject by ignore the static 2 columns 
      subjectLeng = len(headers) - 2
      studentsLeng = len(students) 
      global subjectNumber 
      global studentRollNumber 

      # take the subject number and make sure that he enter the right number 
      subjectNumber = int(input("\n C1 = 1 \n Python = 2 \n DS = 3 \n Please Enter Subject Number :  "))
      while subjectNumber < 1 or subjectNumber > subjectLeng:
            print(f"Invalid input! Please enter a number between 1 and {subjectLeng}.")
            subjectNumber = int(input("Please Enter Subject Number: "))

      #take the number of absent student 
      studentRollNumber = int(input("Please Enter Student Roll Number: "))
      while studentRollNumber < 1 or studentRollNumber > studentsLeng:
            print(f"Invalid input! Please enter a number between 1 and {studentsLeng}.")
            studentRollNumber = int(input("Please Enter Student Roll Number: "))
      readAndEditTheAbstentStudenData()

#read exist excel file and edit on it 
def readAndEditTheAbstentStudenData():
      global studentRollNumber 
      global subjectNumber 
      #load the excel file 
      workBookIntial = load_workbook("Students Attendance.xlsx")
      loadSheet = workBookIntial.active
      # take target subject and student rollno and add to them the static value that get me the place of the data in the excel sheet
      target_cell = loadSheet.cell(row=studentRollNumber + 1, column=subjectNumber+2)
      # add the value to the old data and then check it 
      target_cell.value = target_cell.value + 1 if target_cell.value < 3 else  target_cell.value
      workBookIntial.save("Students Attendance.xlsx") 
      againProcess = input(" There is Another Process or you have end your job ? (y/n)")

      if againProcess.lower() == 'y':
            makeStaffChooseSubject()
      elif againProcess == 'n' or againProcess =="N":
            if target_cell.value == 2:
                  sendMail("Warning please care for you attendance")
            elif target_cell.value == 3:
                  sendMail("you have reach the limit for absent")


def sendMail(attachedMsg):
      msg.set_content(attachedMsg)
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
      

createExcel()
makeStaffChooseSubject()

# naming convention, global, using import for method in the class
# 2. oop
# 3. use pydantic to validate user input
# 4. 