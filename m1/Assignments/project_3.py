name = input("Enter your name:")
club = input("Enter your club name: ")

member_number = input("What's your member number?")
points_earned = input("How many points have you earned?")
event_count = input("How many members are there?")
meeting_hours = input("How long do you meet (in hours)?")
is_active = True

print("")
print("Name:", name,"-> type:", type(name))
print(f'Club: {club}', "-> type:", type(club))
print("Member Number:", member_number, "-> type:", type(member_number))
print("Points Earned:", points_earned, "-> type:", type(points_earned))
print("Event Count:", event_count, "-> type:", type(event_count))
print("Meeting Hours:", meeting_hours, "-> type:", type(meeting_hours))
print("Is Active:", is_active, "-> type:", type(is_active))
print("")
 
member_number_text = str(member_number)
event_count_text = str(event_count)
points_text = str(points_earned)
status_text = str(is_active)
 
print("Member Number like text:", member_number_text, "-> type:", type(member_number_text))
print("Event Count like text:", event_count_text, "-> type:", type(event_count_text))
print("Points like text:", points_text, "-> type:", type(points_text))
print("Status like text:", status_text, "-> type:", type(status_text))

first3_letters = name[0:3]
last_letter = name[-1:]
badge_code = first3_letters + last_letter
 
print("First 3 letters of name:", first3_letters)
print("Last letter of name:", last_letter)
print("Badge Code:", badge_code)

reversed_club = club[::-1]
print("Reversed Club Name:", reversed_club)

badge_line_1 = "CLUB MEMBER" + badge_code
badge_line_2 = "ID: " + member_number_text + " | EVENTS: " + event_count_text
badge_line_3 = "POINTS: " + points_text + " | ACTIVE: " + status_text
badge_line_4 = "SECRET CLUB CODE: " + reversed_club

print("")
print("☺☺☺☺☺☺SCHOOL CLUB MEMBER BADGE☺☺☺☺☺☺")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺")
print("")