sum = 0  
count = 0  

while True:
    grade_input = input("Enter a grade (or type 'exit' to calculate the average): ")
    
    if grade_input == 'exit':
        break
    
    try:
        grade = float(grade_input)
        if 0 <= grade <= 20:
            sum += grade
            count += 1
        else:
            print("Invalid grade. Grade should be between 0 and 20.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if count > 0:
    average = sum / count
    print("Average grade: ", average)
else:
    print("No grades entered.")