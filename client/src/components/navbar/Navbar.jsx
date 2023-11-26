import React, { useState } from 'react';
import { RiMenu3Line, RiCloseLine } from 'react-icons/ri';
import logo from '../../assets/logo.svg';
import './navbar.css';

import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';

const Navbar = () => {
    const [toggleMenu, setToggleMenu] = useState(false);
    const [loggedIn, setLoggedIn] = useState(false);

    const firebaseConfig = {
        apiKey: "AIzaSyATKvYH3M0ebWOgC63i-91HFTUv81I77lU",
        authDomain: "westernhacks-1189e.firebaseapp.com",
        projectId: "westernhacks-1189e",
        storageBucket: "westernhacks-1189e.appspot.com",
        messagingSenderId: "290762197628",
        appId: "1:290762197628:web:97a20e23b0241adf8857f9",
        measurementId: "G-NJGQQLYWD5"
      };
    
    firebase.initializeApp(firebaseConfig);

    const signInWithGoogle = () => {
    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithPopup(provider)
        .then((result) => {
        // Signed in successfully
        const user = result.user;
        console.log('Signed in successfully:', user);
        console.log('Firebase User ID:', user.uid);
        console.log('Firebase Display Name: ', user.displayName)
        localStorage.setItem('uid', JSON.stringify(user.uid));
        localStorage.setItem('name', JSON.stringify(user.displayName));
        setLoggedIn(!loggedIn)
        })
        .catch((error) => {
        // Sign in failed
        console.error('Sign in with Google failed:', error);
        });
    };
    
    const signOut = () => {
    firebase.auth().signOut()
        .then(() => {
            localStorage.setItem('name', null)
        console.log('Signed out successfully');
        setLoggedIn(!loggedIn)
    })
        .catch((error) => {
        console.error('Sign out failed:', error);
    });
    };
 
  
    return (
      <div className="web__navbar">
        <div className="web__navbar-links">
          <div className="web__navbar-links_logo">
            <img src={logo} />
          </div>
          <div className="web__navbar-links_container">
            <p><a href="#home">Home</a></p>
            <p><a href="#wweb">Features</a></p>
            <p><a href="#possibility">Possibilities</a></p>
          </div>
        </div>
        <div className="web__navbar-sign">
            {loggedIn ? (
                <button type="button" onClick={signOut}>Logged In</button>
            ) : (<button type="button" onClick={signInWithGoogle}>Sign Up</button>)}
        </div>
        <div className="web__navbar-menu">
          {toggleMenu
            ? <RiCloseLine color="#fff" size={27} onClick={() => setToggleMenu(false)} />
            : <RiMenu3Line color="#fff" size={27} onClick={() => setToggleMenu(true)} />}
          {toggleMenu && (
          <div className="web__navbar-menu_container scale-up-center">
            <div className="web__navbar-menu_container-links">
                <p><a href="#home">Home</a></p>
                <p><a href="#wweb">Features</a></p>
                <p><a href="#possibility">Possibilities</a></p>
            </div>
            <div className="web__navbar-menu_container-links-sign">
              <button type="button">Sign up</button>
            </div>
          </div>
          )}
        </div>
      </div>
    );
  };
export default Navbar;