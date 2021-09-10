score = 0
number_of_questions = 5

# Question 1
print("Question 1: What is the tallest structure in the world? Type the letter of the option choice to answer.", '\n', "A) Tokyo Skytree", '\n', "B) Burj Khalifa", '\n', "C) Canton Tower", '\n', "D) Abraj Al Bait")
answer = input().lower()
if answer == "b":
    print("Correct!", '\n')
    score += 1
else:
    print("Incorrect.", '\n')

# Question 2
print("Question  2:  Is thie following statement true or false? The sun is a star.", '\n',  "True", '\n', "False")
answer = input().lower()
if answer == "true":
    print("Correct!", '\n')
    score += 1
else:
    print("Incorrect.", '\n')

# Question 3
print("Question 3: Fill in the blank to complete Mr. Adam's infamous quote!", '\n' "Eary is on time, on time is late, and ____ is never acceptable!")
answer = input().lower()
if answer == "late":
    print("Correct!", '\n')
    score += 1
else:
    print("Incorrect.", '\n')

# Question 4
print("Question 4: What is the sum of 2+2 ?")
answer = input().lower()
if answer == "4":
    print("Correct!", '\n')
elif answer == "four":
    print("Correct!", '\n')
    score += 1
else:
    print("Incorrect.", '\n')

# Question 5
print("In what year did the first cat go to space?")
answer = input().lower()
if answer == "1963":
    print("Correct!", '\n')
    score +=1
else:
    print("Incorrect.", '\n')

print("Your score is", score, "out of", number_of_questions, "which is", str(score/number_of_questions * 100) + "%")