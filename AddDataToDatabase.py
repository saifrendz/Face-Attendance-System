import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://faceattendence-6b08a-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "69057":
        {
            "name": "Linus Torvalds",
            "major": "Linux OS",
            "starting_year": 2017,
            "total_attendance": 14,
            "standing": "G",
            "year":7,
            "last_attendance_time": "2024-03-21 00:54:34"
        },
    "70110":
        {
            "name": "Bill Gates",
            "major": "Windows",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "G",
            "year":5,
            "last_attendance_time": "2024-03-15 00:54:34"
        },
    "93588":
        {
            "name": "Saifur Rehman",
            "major": "Ethical hacking",
            "starting_year": 2023,
            "total_attendance": 6,
            "standing": "G",
            "year":2,
            "last_attendance_time": "2024-03-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)