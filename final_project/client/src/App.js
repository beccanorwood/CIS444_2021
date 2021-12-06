import './App.css';
import React, {useEffect} from 'react';

import {AddFriend} from './components.js/AddFriend';
import {UserAuth} from './components.js/UserAuth'
import {SignUp} from './components.js/SignUp';
import {Simple} from './components.js/Restaurants';

function App() {

  return (
    <div className="App">
        <h2>iDunno?</h2>
        <div className='row'>
          <p><Simple/></p>
        </div>
    </div>
  )
}

export default App;
