# List of questions
questions = [
    "What is your name?",
    "What is your favorite color?",
    "What is your favorite food?",
    "What is your favorite hobby?",
    "What is your dream job?"
]

# List to store answers
answers = []

# Ask each question and collect the answer
for question in questions:
    answer = input(question + " ")
    answers.append(answer)

# Display questions and answers together as the final result
print("\n--- Final Results ---")
for i in range(len(questions)):
    print(f"{questions[i]} : {answers[i]}")
