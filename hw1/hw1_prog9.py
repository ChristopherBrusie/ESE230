# asking for scores in each category
ice_score = float(input("Enter your total ICE score out of 250: "))
exam1 = float(input("Enter your score for Exam 1 out of 40: "))
exam2 = float(input("Enter your score for Exam 2 out of 40: "))
exam3 = float(input("Enter your score for Exam 3 out of 40: "))
orientation_quiz = float(input("Enter your score for the orientation quiz out of 40: "))
lab_score = float(input("Enter your total lab score out of 1000: "))
hw_score = float(input("Enter your total homework score out of 500: "))

# calculate percentage scores
ice_pct = (ice_score/250)*20
exam_pct = ((exam1 + exam2 + exam3)/120)*33
quiz_pct = (orientation_quiz/40)*2
labs_pct = (lab_score/1000)*25
hw_pct = (hw_score/500)*20

# calculate final percentage
final_pct = ice_pct + exam_pct + quiz_pct + labs_pct + hw_pct

# determine letter grade range
if final_pct >= 85:
    grade_range = "A"
elif final_pct >= 70:
    grade_range = "B"
elif final_pct >= 60:
    grade_range = "C"
elif final_pct >= 50:
    grade_range = "D"
else:
    grade_range = "Fail"
    
#display the result
print(f"Your final percentage sscore is {final_pct:.2f}%. This is in the {grade_range} range. \nThe instructor will decide if it is {grade_range}+, {grade_range}, or {grade_range}-. ")
