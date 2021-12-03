import './App.css';
import React, {useEffect} from 'react';

function App() {

  useEffect(() => {
    fetch('/open_api/test')
    .then((response) => response.json())
    .then((data) => console.log(data)); 
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <h3>Test</h3>
      </header>
    </div>
  );
}

export default App;