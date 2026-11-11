class TakeAbsentData:
      def __init__(self , student_count , subject_count):
           self.student = None
           self.subject = None
           self.student_count = student_count
           self.subject_count = subject_count

      def set_student(self,value):
            int_cast_value = int(value)
            while int_cast_value < 1 or int_cast_value > self.student_count or len(value) == 0 or value.strip() == 0:
                  print(f"Invalid input! Please enter a number between 1 and {self.student_count}.")
                  value = input("Please Enter Student Roll Number: ")
            self.student = int(value)
      
      def set_subject(self,value):
            int_cast_value = int(value)
            while int_cast_value < 1 or int_cast_value > self.subject_count or len(value) == 0 or value.strip() == 0:
                  print(f"Invalid input! Please enter a number between 1 and {self.subject_count}.")
                  value = input("Please Enter Subject Number: ")
            self.subject = int(value)