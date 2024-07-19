# This is the Student grade calculator

# getting student names and  grades from user 


# function to calculate average


# function for highest and lowest grade


# function for displaying result



# ----Code starts here-----#



print("Welcome to Student Grade Calculator\n")



def student_data():
    data = {}
    while True:
             
        name =input("enter students name (or write done to finish)\n" )
          
        if name.lower()=='done':
              break    
                      
        try:
         marks =float(input("please enter student marks \n"))  
         data[name] = marks;    
        except ValueError :
              print("please provide a number for marks");
   
    return data   
    
    



def  Student_average(data):
    
    total_marks =sum(data.values())
    
    no_of_students =len(data)
    
    
    if no_of_students == 0:
        
        print("please enter some student data")
        
    average =total_marks/no_of_students
    
    return average

    
        
        
        
# print("the average student marks  is ", Student_average());    
        
  
  
def  student_marks(data):
        
    if not data  :
        
      return None
         
    else:
        
     highest_marks = max(data.values())
    
        
     lowest_marks = min(data.values())
    
    
    return highest_marks , lowest_marks
    
    
    
    
# print("the highest and lowest student marks  are ", student_marks());    



def  result(data):
    
    average = Student_average(data)
    highest, lowest = student_marks(data)
    
    if average is not None:
        print("\n--- Student Marks Report ---")
        print("Average Marks: ", average)
        for name, marks in data.items():
            if marks == highest:
                print(f"Highest Marks: {marks} (by {name})")
            if marks == lowest:
                print(f"Lowest Marks: {marks} (by {name})")

    



# Main code
print("Welcome to Student Grade Calculator\n")
students = student_data()
result(students)