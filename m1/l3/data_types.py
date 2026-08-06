# Agent
# line 2

"""
Output:
Agent name: Dheeksha
Agent number: 4

Badge/code: Dhha4
-----------------------------
Agent name: Ajay
Agent number: 56

Badge/code: Ajay56

name = Pineapple

word1 = name[0:4]
word2 = name[-3:]


"""

name = input("What's your name? ")
agent_number = input("What's your agent number?")

print(type(name))
print(type(agent_number))

word1 = name[0:2]
word2 = name[-2:]

badge = word1 + word2 + agent_number
print(f"Your badge is: {badge}")

