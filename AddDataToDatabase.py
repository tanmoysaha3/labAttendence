import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://just-digital-diary-9503d-default-rtdb.europe-west1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34",
            "last_exit_time": "2022-12-11 00:54:34",
            "last_arrival_time": "2022-12-11 00:24:34",
            "status": "out"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34",
            "last_exit_time": "2022-12-11 00:54:34",
            "last_arrival_time": "2022-12-11 00:24:34",
            "status": "out"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34",
            "last_exit_time": "2022-12-11 00:54:34",
            "last_arrival_time": "2022-12-11 00:24:34",
            "status": "out"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
