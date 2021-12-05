import './App.css';
//import { secure_get_with_token } from './cis444'
import React, {useEffect} from 'react';

import { AddFriend } from './conponents.js/AddFriend';
import {UserAuth} from './conponents.js/UserAuth'
import {SignUp} from './conponents.js/SignUp'

function App() {

  /*useEffect(() => {
    fetch('/open_api/test')
    .then((response) => response.json())
    .then((data) => console.log(data))
  }, []);


  /*useEffect(() => {
    secure_get_with_token(fetch('/secure_api/get_restaurants', {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({title: 'Test POST Request'})
    })
      .then((response) => response.json())
      .then((data) => console.log(data)));
  }, []);*/


  return (
    <div className="App">
      <header className="App-header">
        <h2>iDunno?</h2>
        <section><AddFriend/></section>
      </header>
    </div>
  );
}

export default App;
