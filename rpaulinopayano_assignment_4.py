#beginning of step 1
student_name = "Rayner Paulino-Payano"
current_gpa = 0.00
study_hours = 20
social_points = 50
stress_levels = 30

print("=== Welcome ===")
print("Here are your starting stats:")
print(f"Your name is: {student_name}")
print(f"Your current gpa is: {current_gpa}")
print(f"The number of hours you study per week is: {study_hours}")
print(f"Your number of social points is (on a scale of 0 -100): {social_points}")
print(f"Your current stress level is (on a scale of 0 - 100): {stress_levels}")
#end of step 1

#Beginning of step 2
print("Hello. Please enter your current gpa (more than 0.0 and less than 4.0) to receive a course load recommendation.")
current_gpa = float(input())

if current_gpa >= 3.7:
    study_hours = 25 #smart student gets heavy course load recommended
    stress_levels = 100
    recommended_credits = 18
elif current_gpa >= 2.8:
    study_hours = 20 #average level student gets regular couse load
    stress_levels = 50
    recommended_credits = 15
else:
    study_hours = 10 #low intelligence student gets low course load
    stress_levels = 20
    recommended_credits = 12

print(f"Based on your GPA of {current_gpa} we recommend the following:")
print(f"Recommended course load: {recommended_credits} credits")
print(f"Estimated Weekly Study Hours: {study_hours}")
print(f"Estimated Stress level based on course load: {stress_levels}")
print()
#end of step 2

#beginning of step 3
study_options = ["Programming", "Math", "English", "History"]

print(f"Available subjects for the study session: {study_options}")
user_choice = input("Which subject do you want to focus on? ")

if user_choice in study_options:
        print(f"\nGood choice! Focusing on {user_choice} is a great idea.")
        
        # if statements for study strategy
        if user_choice == "Programming" and current_gpa >= 3.5:
            # high achieving student with hard subject
            print("Given your high GPA, consider going into a difficult topic or starting a new project.")
            print("You are in a good position to do great!")
        
        elif current_gpa < 2.5 or social_points < 50:
            # if gpa is low or social life is low, recommend a balance of both
            print("A balanced approach is key. You should dedicate solid study time to this subject,")
            print("but also remember to take breaks and recharge.")
        
        elif not (current_gpa < 3.0 and social_points > 70):
            # If not (low GPA AND high social points)  suggest a productive study session
            print("you have a good balance. A focused and productive study session is recommended")

        else:
            # Fallback for other combinations
            print("This is a good plan. Keep up the good work!")       
else:
    #Invalid choice
    print("\nthat subject is not on the list. Please choose one from the available options")
    print()
#end of step 3

