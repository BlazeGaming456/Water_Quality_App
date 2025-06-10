import pyrebase

config = {
  'apiKey': "AIzaSyBN8bbOD-WtxvthDQnSnCoOxYrmOYYDwHw",
  'authDomain': "water-quality-35f40.firebaseapp.com",
  'databaseURL': "https://water-quality-35f40-default-rtdb.asia-southeast1.firebasedatabase.app/",
  'projectId': "water-quality-35f40",
  'storageBucket': "water-quality-35f40.firebasestorage.app",
  'messagingSenderId': "1076986315358",
  'appId': "1:1076986315358:web:596c17f6055c193667eacf"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()