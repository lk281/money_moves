# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from flask_pymongo import PyMongo
# from model import getImageUrlFrom
import os
from model import question_list, randomize_answers

# -- Initialization section --
app = Flask(__name__)

user_answers = {"question1": "", "question2": "", "question3": "", "question4": "", "question5": ""}

# -- Routes section --

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])

# first page that shows up when the app is run
def homepage():
    # global user_answers 
    # user_answers = {"question1": "", "question2": "", "question3": "", "question4": "", "question5": ""}
    return render_template('index.html')


@app.route('/')
@app.route('/question1', methods=['POST', 'GET'])

def question_one():
    question = question_list[0]
    random_answers, answers_dictionary = randomize_answers(question)
    first_answer = random_answers[0]
    second_answer = random_answers[1]
    third_answer = random_answers[2]
    return render_template('question1.html', question = question, first_answer=first_answer, second_answer=second_answer, third_answer=third_answer, answers_dictionary = answers_dictionary)


@app.route('/')
@app.route('/question2', methods=['GET', 'POST'])

def question_two():
    question = question_list[1]
    random_answers, answers_dictionary = randomize_answers(question)
    first_answer = random_answers[0]
    second_answer = random_answers[1]
    third_answer = random_answers[2]
    if request.method == 'POST': 
        answer = request.form['Q1']
        if answer == "1":
            user_answers["question1"] = "correct"
        else: 
            user_answers["question1"] = "wrong"
    return render_template('question2.html', question = question, first_answer=first_answer, second_answer=second_answer, third_answer=third_answer, answers_dictionary = answers_dictionary)


@app.route('/')
@app.route('/question3', methods=['GET', 'POST'])

def question_three():
    question = question_list[2]
    random_answers, answers_dictionary = randomize_answers(question)
    first_answer = random_answers[0]
    second_answer = random_answers[1]
    third_answer = random_answers[2]
    if request.method == 'POST': 
        answer = request.form['Q1']
        if answer == "1":
            user_answers["question2"] = "correct"
        else: 
            user_answers["question2"] = "wrong"
    return render_template('question3.html', question = question, first_answer=first_answer, second_answer=second_answer, third_answer=third_answer, answers_dictionary = answers_dictionary)

@app.route('/')
@app.route('/question4', methods=['GET', 'POST'])
def question_four():
    question = question_list[3]
    random_answers, answers_dictionary = randomize_answers(question)
    first_answer = random_answers[0]
    second_answer = random_answers[1]
    third_answer = random_answers[2]
    if request.method == 'POST': 
        answer = request.form['Q1']
        if answer == "1":
            user_answers["question3"] = "correct"
        else: 
            user_answers["question3"] = "wrong"
    return render_template('question4.html', question = question, first_answer=first_answer, second_answer=second_answer, third_answer=third_answer, answers_dictionary = answers_dictionary)

@app.route('/')
@app.route('/question5', methods=['GET', 'POST'])
def question_five():
    question = question_list[4]
    random_answers, answers_dictionary = randomize_answers(question)
    first_answer = random_answers[0]
    second_answer = random_answers[1]
    third_answer = random_answers[2]
    if request.method == 'POST': 
        answer = request.form['Q4']
        if answer == "1":
            user_answers["question4"] = "correct"
        else: 
            user_answers["question4"] = "wrong"
    return render_template('question5.html', question = question, first_answer=first_answer, second_answer=second_answer, third_answer=third_answer, answers_dictionary = answers_dictionary)

@app.route('/')
@app.route('/results', methods=['GET', 'POST'])

def result():

    if request.method == 'POST': 
        answer = request.form["Q5"]
        if answer == "1":
            user_answers["question5"] = "correct"
        else: 
            user_answers["question5"] = "wrong"

    score = 0

    for key in user_answers.keys(): 
        print(key)
        print(user_answers[key])
        if user_answers[key] == "correct":
            score += 1
    return render_template('results.html', score = score)