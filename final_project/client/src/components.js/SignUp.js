import React, {useState, useEffect} from 'react';

function SignUp() {

    /**
     * Local variables keeping track of user input 
     */
    const [u_username, setUsername] = useState("");
    const [u_password, setPassword] = useState("");
    const [u_firstname, setFirstName] = useState("");
    const [u_lastname, setLastName] = useState("");


    return (
    <>
        <div className="ui placeholder segment">
            <div className="column">
            <div className="ui form">
                <div className="field">
                <label>First Name</label>
                <div className="ui left icon input">
                    <input type="text" value = {u_firstname} onChange={(event) => {setFirstName(event.target.value)}}/>
                </div>
                </div>
                <div className="field">
                <label>Last Name</label>
                <div className="ui left icon input">
                    <input type="text" value = {u_lastname} onChange={(event2) => {setLastName(event2.target.value)}}/>
                </div>
                </div>
                <div className="field">
                <label>Username</label>
                <div className="ui left icon input">
                    <input type="text" value = {u_username} onChange={(event3) => {setUsername(event3.target.value)}}/>
                    <i className="user icon"></i>
                </div>
                </div>
                <div className="field">
                <label>Password</label>
                <div className="ui left icon input">
                    <input type="password" value = {u_password} onChange={(event4) => {setPassword(event4.target.value)}}/>
                    <i className="lock icon"></i>
                </div>
                </div>
                <button className="fluid ui violet button" onClick = {async() => CheckCreds(u_username, u_password)}>SignUp</button>
            </div>
            </div>
        </div>
    </>
    )

}

async function CheckCreds(u_username, u_password) {
    
    const response = await fetch('/open_api/signup,', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'
    },
        body: JSON.stringify({username: u_username, password: u_password})
    })

    if (response.ok) {
        console.log("It Worked!");
    }
} 



export {SignUp}