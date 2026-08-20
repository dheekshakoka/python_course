print('\n study time calculation🙂\n')

# Ask for wake-up time
wake_up_time = input("What time do you wake up? ")
print("waking up at", wake_up_time)

# Check if there's enough time to study
if wake_up_time == "6:00 AM" or wake_up_time == "6:30 AM" or wake_up_time == "7:00 AM":
    print("You have enough time to study before school.")
else:
    print("You might not have enough time for studying before school.")

# Print daily routine steps
print("going to school")
school = input("Are you going to school today? (yes/no) ")
if school == "yes": print ("good girl😊")
else: print ("bad girl😡")
print("playing")
# Ask about playing
play_time = int(input("How many hours do you play per day? "))
print("You play", play_time, "hours per day.")

# Check if play time is healthy
if play_time <= 2:
    print("That is a good amount of playing time! 😊")
else:
    print("That is too much playing time, you will become addicted! 😡")

# Simple guessing game
print("\nLet's play a guessing game!")
secret_number = 5
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret_number:
    print("You got it right! The number was", secret_number)
else:
    print("You are wrong 😑, the number was", secret_number)
print("studying")

# Ask for daily study hours
daily_study_hours = int(input("\nHow many hours do you study per day? "))

# Calculate total study time in a week using arithmetic
total_study_time = daily_study_hours * 7
print("Total study time in a week:", total_study_time, "hours.")
print("study time calculation completed😁🤩")