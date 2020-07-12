import pyrebase

config = {
    "apiKey": "AIzaSyCJmDfLiSa1tmXB343uZnYC4TRB7dpiDqE",
    "authDomain": "belajar-python-280014.firebaseapp.com",
    "databaseURL": "https://belajar-python-280014.firebaseio.com",
    "projectId": "belajar-python-280014",
    "storageBucket": "belajar-python-280014.appspot.com",
    "messagingSenderId": "680677519859",
    "appId": "1:680677519859:web:647998513a8f5daa2da286",
    "measurementId": "G-N9GLH520GP"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
