attendance = float(input("Enter your attendance percentage: "))
avg_grade = float(input("Enter your average grade: "))

if attendance >= 75 and avg_grade >= 50:
    print("You are eligible for the exam.")

elif attendance < 75:
    reason = input(" Do you have a medical reason? yes/no: ")
    
    if reason == "yes" and avg_grade >= 50:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible to sit for the exam.")

elif avg_grade < 50:
    print("You are not eligible for the exam.")