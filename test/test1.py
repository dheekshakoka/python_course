"""
1 Project × 40 Marks

Number Guessing Game
Build a game where the computer picks a secret number between 1 and 50. You have 5 attempts to guess it. After every wrong guess your program shows a hint telling you how close you are. Remaining lives are shown as hearts after each attempt.

💡 Hint: Store your secret number in a variable — for example: secret = 27



If you already know the random module, feel free to use it! This test checks your logic (conditions, loops, input/output).


What you need to use
------------------------------------------------------------------------
1.  int(input())       →  to read the player's guess
2.  while loop         →  stops after 5 attempts or when player wins
3.  if/elif/else       →  hint system —

🧊 ice cold, 🥶 cold, 🌡️ warm, or 🔥 hot


4.  for loop           →  shows 

remaining ❤️ hearts

 after each wrong guess
5.  win/loss message   →  reveals the secret number if attempts run out
------------------------------------------------------------------------

What you'll be marked on
------------------------------------------------------------------------
1.  Program runs without any errors                          →   5 marks
2.  int(input()) used to read the player's guess             →   5 marks
3.  while loop stops after 5 attempts or on correct guess    →  10 marks
4.  Hint system prints ice cold / cold / warm / hot          →  10 marks
5.  for loop shows correct hearts after each wrong guess     →   5 marks
6.  Win message shown / secret revealed if attempts run out  →   5 marks
========================================================================
Total  →  40 marks
========================================================================

"""

secret = 10
attempts = 5
for i in range(5):
    guess = int(input("choose a number: "))
    if guess > secret:
        print("try lower")
        attempts -= 1
        print("remaining attempts:", attempts)
    elif guess < secret:
        print("try higher")
        attempts -= 1
        print("remaining attempts:", attempts)
    elif guess == secret:
        print("you got the right answer")
        break
    elif attempts == 0:
        break
print("Your attempts are over")
        
