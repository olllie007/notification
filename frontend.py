#for the http requests
import requests
from flask import request
from tkinter import *
root = Tk()
root.title("notification")
BASE = 'http://127.0.0.1:5000/'
global title, body
def master():
    #send the notifcation to be stored
    notification_title = title.get()
    notification_body = body.get()
    requests.post(BASE + 'master/' + notification_title + '/' + notification_body)
    pass
def post():
    
    global title, body
    name = entry.get()
    #give mster controls
    if name == 'master':
        title_text = Label(root, text='Title')
        title_text.pack()
        title = Entry(root, width=50, bg='red', borderwidth=10)
        title.pack()
        body_text = Label(root, text='Body')
        body_text.pack()
        body = Entry(root, width=50, bg='red', borderwidth=10)
        body.pack()
        not_submit = Button(root, text='Submit', command=master)
        not_submit.pack()
    #get the notification back from the data base
    else:
        response = requests.get(BASE + 'person')
        response = response.json()
        notification = Label(root, text=response)
        notification.pack()

#tkinter gui setup
entry = Entry(root, width=50, bg='red', borderwidth=10)
entry.pack()
submit = Button(root, text='Submit', command=post)
submit.pack()

