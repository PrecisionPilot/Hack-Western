import React from 'react';
import possibilityImage from '../../assets/possibility.png';
import './possibility.css';

const Possibility = () => (
  <div className="web__possibility section__padding" id="possibility">
    <div className="web__possibility-image">
      <img src={possibilityImage} alt="possibility" />
    </div>
    <div className="web__possibility-content">
      <h1 className="gradient__text">The possibilities are <br /> beyond your imagination</h1>
      <br/>
      <p>With the endless possibilities of scrolling, clicking, and voice automation, you can control everything on your computer using just your face – and when it's time to relax, take a break from this digital world.</p>
    </div>
  </div>
);

export default Possibility;