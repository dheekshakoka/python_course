# Classroom Points Calculator
"""
Author: Dheeksha Koka
Date: 12/08/2026

This program is for calculating how many points are earned,
what the total amount of reward stars are and in how many boxes you can pack them.
finally, you compare the results with last week, see what the total
amaunts after adding and removing points and you calculate the final
amount of boxes packed.
"""

team1 = 150
team2 = 86
team3 = 124
team4 = 98
team5 = 87

# Calculate total and average
total = team1 + team2 + team3 + team4 + team5
average = total / 5
 
print("The total points are:", total)
print("The average per team are:", average)

 # Each point gives 2 stars
stars_per_point = 2
reward_stars = total * stars_per_point
print("The total reward stars are:", reward_stars)

# The stars are packed in boxes of 25 each
boxes = reward_stars // 25
remaining = reward_stars % 25
 
print("Full boxes packed:", boxes)
print("Leftover stars:", remaining)

 # Compare with last week
last_week = 500
 
print("Better than last week?:", total > last_week)
print("Same as last week?:", total == last_week)
print("At least as good as last week?:", total >= last_week)

 # Total points after adding bonus points
total += 30
print("After bonus points:", total)
 
# Total points after removing points for missed tasks
total -= 15
print("After missed tasks :", total)
 
# Final reward box count after all changes
reward_stars = total * stars_per_point
boxes = reward_stars // 25

 
print("Final boxes packed :", boxes)
