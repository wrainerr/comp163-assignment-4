#beginning of step 1
student_name = "Rayner Paulino-Payano"
current_gpa = 3.00
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
print()
#end of step 1

#Beginning of step 2
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
print("D) Double Major (21 credits)")
choice = input("Your choice: ")

if choice == "A":
    recommended_credits = 12
    study_hours = 15
    stress_level = 20
    print("You've chosen a light course load. This will allow for more time outside of academics.")
elif choice == "B":
    recommended_credits = 15
    study_hours = 20
    stress_level = 50
    print("A standard course load is a balanced choice for a typical semester.")
elif choice == "C":
    recommended_credits = 18
    study_hours = 30
    stress_level = 80
    print("This is a heavy course load. Be prepared for a significant time commitment.")
elif choice == "D":
    recommended_credits = 21
    study_hours = 45
    stress_level = 100
    print("A double major load is very demanding and will challenge your time management skills.")
else:
    # handle invalid input
    print("Invalid choice. Please select 'A', 'B', 'C', or 'D' to continue.")
    recommended_credits = 0 # Set to a value that will indicate an error or non-choice.

#  the outcome of Step 2
if recommended_credits != 0:
    print(f"\nBased on your choice, your estimated stats are now:")
    print(f"Recommended course load: {recommended_credits} credits")
    print(f"Estimated Weekly Study Hours: {study_hours}")
    print(f"Estimated Stress Level: {stress_level}")
#end of step 2

#beginning of step 3
study_options = ["Programming", "Math", "English", "History"]

print()
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

#beginning of step 4
# default ending message that will be used if no special ending is triggered (for the resilient path)
status_message_template = "Your journey shows that learning is about growth and being able to adapt. Keep exploring, keep growing, and you will achieve great things."

# This variable will hold the final message. the default value is the template above
final_message = status_message_template

print("You are now at the final stage of your academic journey. Let's review your path.")
print()

if(recommended_credits == 18):
    print("You chose a heavy course load. Good luck!")
    if user_choice == "Programming" and current_gpa >= 3.7:
        print("Your high GPA and focus on a challenging subject show great potential.")
    else:
        print("Managing a heavy load requires discipline. Stay focused.")
elif recommended_credits == 15:
        print("You chose a standard, balanced course load.")
else:
    print("You chose a light course load, making sure your foundations are solid.")

#now for the three endings:

print("\nChoosing your final outcome...")
print()
    
# Ending 1: Exceptional achievement
if current_gpa >= 3.7 and recommended_credits == 18 and user_choice == "Programming":
    final_message = "The Exceptional Achiever! Your dedication to a heavy course load, combined with a focus on a high-demand subject and an outstanding GPA, points to an incredibly successful academic career. You are a great student!"

# Ending 2: Balanced success
elif current_gpa >= 2.8 and social_points >= 50 and recommended_credits == 15:
    final_message = "The Well-Rounded Success! You've found the perfect balance between academics and social life. Your solid GPA, active social engagement, and balanced course load mean you are on track for a fulfilling and successful experience. Well done!"

# this checks if the final_message variable is still the exact same object as the template. if it is, it chooses the resilient path (default path)
if final_message is status_message_template:
    print("\n*** The Resilient Path! ***")
else:
    # If the variables are not the same object, it means a new message was assigned
    if not("Exceptional" not in final_message):
        print("\n*** The Exceptional Achiever! ***")
    elif not("Well-Rounded" not in final_message):
        print("\n*** The Well-Rounded Success! ***")

print(final_message)

    # final stats
print("\n--- Final Statistics ---")
print(f"Final GPA: {current_gpa}")
print(f"Final Social Points: {social_points}")
print(f"Selected Course Credits: {recommended_credits}")
print(f"Subject of Focus: {user_choice}")
