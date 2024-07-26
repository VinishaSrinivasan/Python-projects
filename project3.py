# QUIZ GAME #

questions = [
    {
        "que" : "What is the oldest language in the world?",
        "options" : ["A.English","B.Tamil","C.French","D.Spanish"],
        "answer" : "B"
    },
    {
        "que" : "In 2011, india won the world cup T50 after how many years?",
        "options" : ["A.10 years","B.2 years","C.25 years","D.27 years"],
        "answer" : "D"
    },
    {
        "que" : "In india, which state is larger?",
        "options" : ["A.UttarPradesh","B.TamilNadu","C.Rajastan","D.Delhi"],
        "answer" : "C"
    },
    {
        "que" : "What is the captial of tamilnadu?",
        "options" : ["A.Madurai","B.Chennai","C.Coimbatore","D.Salem"],
        "answer" : "B"

    }
  
]

def quiz_game(questions):
    score = 0
    for question in questions:
        print(question["que"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C or D):").upper()
        if answer == question["answer"]:
            print("Correct,You are great!\n")
            score += 1
        else:
            print("OOPS!!Wrong. The correct answer was", question["answer"],)
    print(f"You got {score} out of {len(questions)} questions correct.")

quiz_game(questions)
