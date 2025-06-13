// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "",
  authDomain: "water-quality-analy.firebaseapp.com",
  databaseURL: "https://water-quality-analy-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "water-quality-analy",
  storageBucket: "water-quality-analy.firebasestorage.app",
  messagingSenderId: "1081306380918",
  appId: "1:1081306380918:web:95523a872f7e6b44c3bd57",
  measurementId: "G-BPB4M3XXVK"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);