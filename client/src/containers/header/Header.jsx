import React from 'react'
import { Link } from 'react-router-dom'
import './header.css';
import web from '../../assets/web.png';


const Header = () => (
    <div className="web__header section__padding" id="home">
      <div className="web__header-content">
        <h1 className="gradient__text">Navigate the Web with Your Gaze</h1>
        <p>Rediscover the joy of effortless browsing, empowering accessibility and inspiring a new era of digital exploration. </p>
  
        <div className="web__header-content__input">
          <a href='https://www.mediafire.com/file/mzxthv06qbh2n34/Hack-Western.zip/file' target='_blank'>
            <button type="button">Download</button>
          </a>
        </div>
  

      </div>
  
      <div className="web__header-image">
        <img src={web} />
      </div>
    </div>
  );
  

export default Header