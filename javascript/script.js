const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
})

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
})

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
})

iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
})

// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-app.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyAq7-ziABaQCTxfeOlMIbv8jvfQk2B7lmQ",
    authDomain: "pbl5-94125.firebaseapp.com",
    databaseURL: "https://pbl5-94125-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "pbl5-94125",
    storageBucket: "pbl5-94125.appspot.com",
    messagingSenderId: "42461525472",
    appId: "1:42461525472:web:e0519d8a1a0e0644f1e785",
    measurementId: "G-K47401613X"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getAnalytics(app);
