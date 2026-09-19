total_homework = 4
original_count = total_homework
print(f"You have {original_count} homework tasks to finish today!\n")
 
completed_count = 0
task_num = 1
 
while task_num <= total_homework:
 

    if task_num == 1:
        next_task = "Math"
    elif task_num == 2:
        next_task = "Science"
    elif task_num == 3:
        next_task = "English"
    else:
        next_task = "Coding"
 
    answer = input(f"Have you finished: {next_task}? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Great job! Homework task completed.")
    else:
        print("Okay, finish it and check again!")
 

    print("Homework tasks remaining:", total_homework - completed_count)



 

print("You completed all your homework")

test_value = 0
safety_counter = 0
 
while test_value <= 0:
    safety_counter += 1
 
    if safety_counter == 3:
        break
 

print("😀😀😀HOMEWORK COMPLETION SUMMARY😀😀😀")
print("Homework Assigned Today:", original_count)
print("Homework Completed:", completed_count)
print("Homework Remaining:", total_homework - completed_count)
print("😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀")