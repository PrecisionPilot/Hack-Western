import React from 'react'
import './what.css';
import Feature from '../../components/feature/Feature';

const What = () => {
  return (
    <div className="web__whatweb section__margin" id="wweb">
    <div className="web__whatweb-feature">
      <Feature title="What is Gazy" text="Gazy empowers individuals with limited mobility by using a webcam to enable hands-free scrolling. By effortlessly tracking gaze movements, it provides an intuitive and inclusive way for all users to navigate digital content, making the web more accessible to all." />
    </div>
    <div className="web__whatweb-heading">
      <h1 className="gradient__text">Give your body the love it deserves</h1>
    </div>
    <div className="web__whatweb-container">
      <Feature title="Scroll" text="Effortlessly scroll through content by looking at that that section of the webpage and blinking to click." />
      <Feature title="Type" text="Automate tasks like doing a Google search and essay writing with just your voice, no keys at all." />
      <Feature title="Relax" text="At fixed time intervals, Gazy reminds your eyes to take a break from the screen, giving you the mental clarity you need." />
    </div>
  </div>
  )
}

export default What