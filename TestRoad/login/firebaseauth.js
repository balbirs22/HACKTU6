// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-app.js";
import {getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword} from "https://www.gstatic.com/firebasejs/10.14.1/firebase-auth.js" 
import{ getFirestore, setDoc, doc} from "https://www.gstatic.com/firebasejs/10.14.1/firebase-firestore.js"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBkT6lR4Q3WBpGrArcBrtQdbfTp-a2c_2c",
  authDomain: "login-form-ca2b8.firebaseapp.com",
  projectId: "login-form-ca2b8",
  storageBucket: "login-form-ca2b8.appspot.com",
  messagingSenderId: "790690195552",
  appId: "1:790690195552:web:267428ce34128f650c7b05"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const signup=document.getElementById('submitSignUp');
signup.addEventListener('click',(event)=>{
    event.preventDefault();
    const email=document.getElementById('rEmail').value;
    const password=document.getElementById('rPassword').value;
    const firstName=document.getElementById('rfName').value;
    const lastName=document.getElementById('rlName').value;
    const auth=getAuth();
    const db=getFirestore();

    createUserWithEmailAndPassword(auth, email, password)
    .then((userCredential)=>{
        const user=userCredential.user;
        const userData={
            email: email,
            firstName: firstName,
            lastName: lastName
        };
    })

})