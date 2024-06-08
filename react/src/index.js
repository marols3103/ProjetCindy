import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import './css/index.css';
import App from './component/app';

ReactDOM.render(
  <React.StrictMode>
      <div>
        <App />
      </div>
  </React.StrictMode>,
  document.getElementById('root')
);
