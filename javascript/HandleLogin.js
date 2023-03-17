//-------------------------------------------------LOGIN HANDLE-------------------------------------------------------//
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-app.js";
import { getDatabase, set, ref, update } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-database.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged  } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-auth.js";


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
const database = getDatabase(app);
const auth = getAuth();
console.log(database);
btnSignUp.addEventListener('click', (e) => {
    console.log('btnSignUp clicked!');
    //Get email, username and password
    var email = document.getElementById('email').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 
            const user = userCredential.user;

            set(ref(database, 'users/' + user.uid), {
                username: username,
                email: email,

            })

            alert('user created!');
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            // ..
            alert(errorMessage);
        });
});

btnSignIn.addEventListener('click', (e) => {
    console.log('btnSignIn clicked!');
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 
            const user = userCredential.user;

            const dt = new Date();
            update(ref(database, 'users/' + user.uid), {
                last_login: dt,
            })
            alert('User logged in!');
            AccessToCameraPage();

        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            alert(errorMessage);
        });
});

function AccessToCameraPage() {
    window.location.assign('AuthPage.html');
}
