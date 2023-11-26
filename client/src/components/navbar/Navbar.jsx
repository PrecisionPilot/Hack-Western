import React, { useState } from 'react';
import { RiMenu3Line, RiCloseLine } from 'react-icons/ri';
import logo from '../../assets/logo.svg';
import './navbar.css';

const Navbar = () => {
    const [toggleMenu, setToggleMenu] = useState(false);
  
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
          <p>Sign in</p>
          <button type="button">Sign up</button>
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
              <p>Sign in</p>
              <button type="button">Sign up</button>
            </div>
          </div>
          )}
        </div>
      </div>
    );
  };
export default Navbar;