#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import getpass
import json
import os

LOGIN_URL = "https://thehuxley.com/api/login"
BASE_URL = "https://thehuxley.com/api/v1/"

def getToken(username, password):
    headers = {
        "Content-type": "application/json"
    }
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(LOGIN_URL, headers=headers, data=json.dumps(data))
    token_json = response.json()
    return token_json["access_token"]

def getScore(access_token, quiz_id, user_id):
    headers = {"Authorization": "Bearer " + access_token}
    res = requests.get(BASE_URL + 'users/' + user_id + '/quizzes', headers=headers)
    quizzes = res.json()
    for quiz in quizzes:
        if str(quiz['id']) == quiz_id:
            return quiz['currentUser']['score'] / quiz['score']
    assert(False)

def getGrades(access_token, quiz_id):
    headers = {"Authorization": "Bearer " + access_token}
    res = requests.get(BASE_URL + 'quizzes/' + quiz_id + '/users', headers=headers)
    users = res.json()
    grades = dict()
    for user in users:
        grades[user['name']] = getScore(access_token, quiz_id, str(user['id']))
    return grades

def main():
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")
    token = getToken(username, password)
    quiz_id = input("Please enter Quiz ID: ")
    print(getGrades(token, quiz_id))

if __name__ == "__main__":
    main()
