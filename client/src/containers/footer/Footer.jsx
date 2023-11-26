import React from 'react';
import './footer.css';

const Footer = () => (
  <div className="web__footer section__padding">
    <div className="web__footer-heading">
      <h1 className="gradient__text">Browse effortlessly</h1>
    </div>
    
    <a href='https://www.mediafire.com/file/mzxthv06qbh2n34/Hack-Western.zip/file' target='_blank'>
        <div className="web__footer-btn">
        <p>Get Started</p>
        </div>
    </a>

    <div className="web__footer-copyright">
      <p>@2023 Gazy. All rights reserved.</p>
    </div>
  </div>
);

export default Footer;