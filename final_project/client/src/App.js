import './App.css';
//import { secure_get_with_token } from './cis444'
import React, {useEffect} from 'react';

import {AddFriend} from './components.js/AddFriend';
import {UserAuth} from './components.js/UserAuth'
import {SignUp} from './components.js/SignUp'

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <h2>iDunno?</h2>
        <section><UserAuth/></section>
      </header>
    </div>
  );
}

export default App;
