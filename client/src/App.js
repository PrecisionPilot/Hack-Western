import React from 'react';

import { Footer, Possibility, Features, What, Header } from './containers';
import { CTA, Navbar } from './components';

import './App.css';


const App = () => (
  <div className="App">
    <div className="gradient__bg">
      <Navbar />
      <Header />
    </div>
    <What />
    <Features />
    <Possibility />
    <CTA />

    <Footer />
  </div>
);

export default App;