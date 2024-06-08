import React from 'react';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';

import Nav from './header/nav';
import Home from './page/home';
import InterfaceViews from './page/interfaceViews';

const App = () => {
  return (
    <Router>
      <div>
        <Nav />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/interfaceViews" element={<InterfaceViews />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
