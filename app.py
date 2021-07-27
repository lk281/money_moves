# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from flask_pymongo import PyMongo
# from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)

#each question is its own dictionary then they are added to a question list 
question1 = {"question": "What is money?", "wrong_answers": ["another word for dollars", "the paper version of coins"], 
"correct_answer": "an asset that people (or institutions) possess, which can be exchanged for goods and services at a certain rate (the price)."}

question2 = {"question": "What is one thing a loan should be used for as a student?", "wrong_answers": ["Paying for a vacation", "Paying for new expensive clothes"], "correct_answer": "Paying for college"}

question3 = {"question": "What is FASFA?", "wrong_answers": [" A loan issued by the government to help pay for college", "The Fast Food Association scholarship that aids in paying off student loans"], "correct_answer": " A Free Application for Federal Student Aid used by college students to determine their eligibility for student financial aid."}

question_list = [question1, question2, question3]

user_answers = {"question1": "", "question2": "", "question3": ""}

# -- Routes section --


# this code is for the homepage (start screen)
@app.route('/')
@app.route('/homepage', methods=['POST', 'GET'])

# first page that shows up when the app is run
def homepage():
    return render_template('homepage.html')

# currently we only have 3 questions - as we put more in the data base we will add more app routes 
@app.route('/')
@app.route('/question1', methods=['POST', 'GET'])

def question_one():
    question = question_list[0]
    if request.method == 'POST': 
        answer = request.form['answer']
        print("here: "+answer)
    return render_template('question1.html', question = question)



@app.route('/')
@app.route('/question2', methods=['GET', 'POST'])

def question_two():
    question = question_list[1]
    if request.method == 'POST': 
        answer = request.form['answer']
        print("here2: "+answer)
        if answer == "correct":
            user_answers["question1"] = "correct"
        else: 
            user_answers["question1"] = "wrong"
    return render_template('question2.html', question = question)


@app.route('/')
@app.route('/question3', methods=['GET', 'POST'])

def question_three():
    question = question_list[2]
    if request.method == 'POST': 
        answer = request.form['answer']
        print("here3: "+answer)
        if answer == "correct":
            user_answers["question2"] = "correct"
        else: 
            user_answers["question2"] = "wrong"
    return render_template('question3.html', question = question)


@app.route('/')
@app.route('/result', methods=['GET', 'POST'])

def result():

    if request.method == 'POST': 
        answer = request.form['answer']
        if answer == "correct":
            user_answers["question3"] = "correct"
        else: 
            user_answers["question3"] = "wrong"
    # initialize the score variable to keep track of score
    score = 0
    # this is what answer.keys() is => [question1, question2, question3]
    # a list of keys for the dictionary user_answers
    # we loop through the keys
    for key in user_answers.keys(): 
        # print(user_answers)
        # ex. for the first loop key = "question1"
        # so we index into our dictionary (user_answers) with the key:
        # user_answers["question1"]

        # we index into the dictionary with the key to check the value at that key 
        # we check if the user got the question right or wrong
        # if it was right we add 1 to the score 
        if user_answers[key] == "correct":
            score += 1
    # after calculating we send the score to the results.html file 
    return render_template('results.html', score = score)