import './App.css';
import {UserAuth} from './components.js/UserAuth';


function App() {

  return (
    <>
      <div className="navbar">
        <div className="ui inverted secondary menu">
          <a className="active item" href = '/'>
            Home
          </a>
          <a className="item" href = '/'>
            Dashboard
          </a>
          <a className="item" href = '/'>
            Contact
          </a>
      </div>
    </div>
      <div className="App">
          <div className='row'>
            <section><UserAuth/></section>
          </div>
      </div>
    </>
  )
}

export default App;
