import random 

#each question is its own dictionary then they are added to a question list 
question1 = {"question": "What is the difference between a credit card and a debit card? ", "wrong_answers": ["Credit cards allow you to spend money by drawing on funds you have deposited at the bank. Debit cards allow you to borrow money from the card issuer up to a certain limit in order to purchase items or withdraw cash. ", "Nothing. They are the same."], 
"correct_answer": "Debit cards allow you to spend money by drawing on funds you have deposited at the bank. Credit cards allow you to borrow money from the card issuer up to a certain limit in order to purchase items or withdraw cash."}

question2 = {"question": "What should be the purpose of an investment?", "wrong_answers": ["To waste money.", "There is no purpose of an investment. "], "correct_answer": "To potentially increase the amount of money you have."}

question3 = {"question": "What is FAFSA?", "wrong_answers": ["A loan issued by the government to help pay for college.", "The Fast Food Association scholarship that aids in paying off student loans."], "correct_answer": " A Free Application for Federal Student Aid used by college students to determine their eligibility for student financial aid."}

question4 = {"question": "What is a credit score?", "wrong_answers": ["It is the maximum amount of money you can spend on your credit card.", "It is the amount of money you have on your debit card."], "correct_answer": "It predicts how likely you are to pay back a loan on time."}

question5 = {"question": "What is Annual Percentage Rate?", "wrong_answers": ["This term refers to a zero percent interest rate.", "This term refers to a yearly interest rate."], "correct_answer": "This term refers to the monthly effective interest rate that is then multiplied by the number of periods within a year."}

question_list = [question1, question2, question3, question4, question5]

def randomize_answers(question_dictionary):
    wrong_answer1 = question_dictionary["wrong_answers"][0]
    wrong_answer2 = question_dictionary["wrong_answers"][1]
    correct_answer = question_dictionary["correct_answer"]

    answers_dictionary = {wrong_answer1: 0, wrong_answer2: 0, correct_answer: 1}
    random_answers = list(answers_dictionary.keys())
    random.shuffle(random_answers)

    return random_answers, answers_dictionary

