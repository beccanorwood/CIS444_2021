import React, {useState, useEffect} from 'react';

function UserAuth() {

    const [u_username, setUsername] = useState("");
    const [u_password, setPassword] = useState("");

    return (
    <>
        <div className="ui placeholder segment">
            <div className="ui two column very relaxed stackable grid">
                <div className="column">
                <div className="ui form">
                    <div className="field">
                    <label>Username</label>
                    <div className="ui left icon input">
                        <input type="text" placeholder="Username" value = {u_username} onChange={(event) => {setUsername(event.target.value)}}/>
                        <i className="user icon"></i>
                    </div>
                    </div>
                    <div className="field">
                    <label>Password</label>
                    <div className="ui left icon input">
                        <input type="password" value = {u_password} onChange={(event2) => {setPassword(event2.target.value)}}/>
                        <i className="lock icon"></i>
                    </div>
                    </div>
                    <button className="fluid ui violet button" onClick = {async() => {CheckCreds(u_username, u_password)}} >Login</button>
                </div>
                </div>
                <div className="middle aligned column">
                <div className="ui big button">
                    <i className="signup icon"></i>
                    Sign Up
                </div>
                </div>
            </div>
            <div className="ui vertical divider">
                Or
            </div>
        </div>
    </>
    )
}


//Method to call flask_api to check login credentials
async function CheckCreds(u_username, u_password) {

    /*useEffect(() => {
        fetch('/open_api/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'
        },
        body: JSON.stringify({username: u_username, password: u_password})
        })
        .then((response) => response.json())
        .then((data) => console.log(data));
    }, [u_username, u_password]);*/


    const response = await fetch('/open_api/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'
    },
        body: JSON.stringify({username: u_username, password: u_password})
    })

    if (response.ok) {
        console.log("It Worked!");
    }

}


export {UserAuth};