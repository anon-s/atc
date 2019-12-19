#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def score(s, t) -> float:
    grade_number = (-14.009*s**4+40.075*s**3-47.792*s**2+25.881*s-4.1549) * \
            (-432.794*t**8+2292.462*t**7-4547.893*t**6+4203.463*t**5-1920.123*t**4+608.067*t**3-276.101*t**2+75.967*t)
    return float(grade_number)


def score_to_grade(grade_number: float) -> str:
    grading_scheme = {'A': 6,
                      'B': 5,
                      'C': 4,
                      'D': 3,
                      'E': 2,
                      'F': 1}
    grade = 'Invalid'
    for key in grading_scheme:
        if grade_number > grading_scheme[key]:
            grade = key
    return grade


def score_to_grade2(grade_number: float) -> str:
    grading_scheme = {'A': 6,
                      'B': 5,
                      'C': 4,
                      'D': 3,
                      'E': 2,
                      'F': 1}
    grade = 'Invalid'
    for key in grading_scheme:
        if grade_number > grading_scheme[key]:
            if grade == 'Invalid':
                grade = key
        print(grade, key, "grade, key")
    return grade


def ask_input(question: str, valid_answers: list, must_valid_answer: bool = True) -> str:  # This function seems useful
    valid = False
    while not valid:
        choice = input(question)
        if choice.upper() in valid_answers:
            valid = True
        if must_valid_answer is False:
            break
        if not valid:
            print(f"Your input isn't valid. Valid inputs are {valid_answers}")
    return choice.upper()


def question() -> None:
    if ask_input('Are you supplying s, t values directly? (Y/N)', ['Y', 'N']) == 'N':
        length_of_skirt = float(input("What's the length of the skirt? (Numbers): "))
        length_of_waist_to_knee = float(input("What's the length of waist to knee? (Numbers): "))
        s = length_of_skirt / length_of_waist_to_knee
        print(f"Your 's' value is {s}")
        length_of_gap = float(input("What's the length of the gap? (Numbers): "))
        length_of_socks = float(input("What's the length of the sock? (Numbers): "))
        t = length_of_gap / length_of_socks
        print(f"Your 't' value is {t}")
    else:
        s = float(input("What's the 's' value? (Numbers): "))
        t = float(input("What's the 't' value? (Numbers): "))
    print('\nCalculating... *beep* *boop*\n')
    grade_number = score(s, t)
    grade = score_to_grade(grade_number)
    print(" Ryouiki score is .....!")
    print(f"Number: {grade_number}")
    print(f"Grade : {grade}")


def welcome():
    print("Welcome to Zettai Ryouiki Calculator")
    print("The credit for the formula goes to /u/Ikarosswings on reddit. Made by Stiles-X")

if __name__ == '__main__':
    welcome()
    question()
