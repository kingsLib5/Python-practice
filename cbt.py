def create_questions():
    """Create a list of questions, each with options and the correct answer."""
    return [
        {"question": "What is the capital of France?",
         "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
         "correct": "C"},
        {"question": "What is 5 + 3?",
         "options": ["A. 5", "B. 8", "C. 9", "D. 15"],
         "correct": "B"},
        {"question": "What is the largest planet in the solar system?",
         "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
         "correct": "C"},
        {"question": "What is the chemical symbol for water?",
         "options": ["A. O2", "B. H2O", "C. CO2", "D. N2"],
         "correct": "B"},
        {"question": "Who wrote 'Hamlet'?",
         "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"],
         "correct": "C"},
        {"question": "Which element has the atomic number 1?",
         "options": ["A. Helium", "B. Hydrogen", "C. Oxygen", "D. Carbon"],
         "correct": "B"},
        {"question": "What is the square root of 64?",
         "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
         "correct": "C"},
        {"question": "What is the currency of Japan?",
         "options": ["A. Dollar", "B. Yen", "C. Won", "D. Euro"],
         "correct": "B"},
        {"question": "Who painted the Mona Lisa?",
         "options": ["A. Leonardo da Vinci", "B. Michelangelo", "C. Raphael", "D. Picasso"],
         "correct": "A"},
        {"question": "What is the speed of light?",
         "options": ["A. 300,000 km/s", "B. 150,000 km/s", "C. 120,000 km/s", "D. 1,000 km/s"],
         "correct": "A"},
        {"question": "What is the capital of Germany?",
         "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Lisbon"],
         "correct": "A"},
        {"question": "Which is the smallest continent?",
         "options": ["A. Africa", "B. Europe", "C. Australia", "D. Antarctica"],
         "correct": "C"},
        {"question": "What is the powerhouse of the cell?",
         "options": ["A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Golgi body"],
         "correct": "B"},
        {"question": "Which organ pumps blood in the human body?",
         "options": ["A. Liver", "B. Heart", "C. Kidney", "D. Lungs"],
         "correct": "B"},
        {"question": "Which is the longest river in the world?",
         "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
         "correct": "A"}
    ]


def run_test():
    """Run the computer-based test."""
    questions = create_questions()
    results = []  # To store user responses and results

    print("Welcome to the Computer-Based Test!")
    print("Answer each question by typing the letter of your choice (A, B, C, D).")

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for option in question["options"]:
            print(option)

        user_answer = input("Your answer: ").strip().upperc()
        correct_answer = question["correct"]

        if user_answer == correct_answer:
            results.append({"question": question["question"], "your_answer": user_answer, "status": "Correct"})
        else:
            results.append({"question": question["question"], "your_answer": user_answer,
                            "correct_answer": correct_answer, "status": "Failed"})

    # Display results
    print("\n--- Test Results ---")
    for i, result in enumerate(results, start=1):
        print(f"\nQuestion {i}: {result['question']}")
        print(f"Your Answer: {result['your_answer']}")
        if result["status"] == "Correct":
            print("Status: Correct")
        else:
            print(f"Correct Answer: {result['correct_answer']}")
            print("Status: Failed")

    print("\nThank you for taking the test!")


if __name__ == "__main__":
    run_test()
