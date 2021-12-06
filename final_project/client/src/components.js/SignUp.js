import React, {useState, useEffect, Component} from 'react';
import { AddFriend } from './AddFriend';


class SignUp extends Component {

    constructor() {
        super();
        this.state = {
            visible: true
        };
        this.onInputChange = this.onInputChange.bind(this);
        this.onSubmitForm = this.onSubmitForm.bind(this);
    }

    onInputChange(e) {
        this.setState({
            [e.target.name]: e.target.value
        });
    }

    onSubmitForm() {
        console.log(this.state);
        console.log(this.state.username);
    }

    async CheckCreds(u_username, u_password, u_firstname, u_lastname) {
    
        const result = await fetch('/open_api/signup', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        },
            body: JSON.stringify({username: u_username, password: u_password, firstname: u_firstname, lastname: u_lastname})
        })
        .then(res => res.json())
        
        
        if (!(result.authenticated)) {
            alert("Username is already taken. Please try again");
        }
        else {
            alert("Succes! You will now be redirected to the next page");
            this.setState({visible: false});
        }

    }

    render() {

        if (!this.state.visible) {
            return <div><AddFriend/></div>
        }

        return (
            <>
                <div className="ui placeholder segment">
                    <div className="column">
                    <div className="ui form">
                        <div className="field">
                        <label>First Name</label>
                        <div className="ui left icon input">
                            <input type="text" name = 'firstname' value = {this.state.name} onChange = {this.onInputChange}/>
                        </div>
                        </div>
                        <div className="field">
                        <label>Last Name</label>
                        <div className="ui left icon input">
                            <input type="text" name = "lastname" value = {this.state.name} onChange = {this.onInputChange}/>
                        </div>
                        </div>
                        <div className="field">
                        <label>Username</label>
                        <div className="ui left icon input">
                            <input type="text" name = "username" value = {this.state.name} onChange = {this.onInputChange}/>
                            <i className="user icon"></i>
                        </div>
                        </div>
                        <div className="field">
                        <label>Password</label>
                        <div className="ui left icon input">
                            <input type="password" name = "password" value = {this.state.name} onChange = {this.onInputChange}/>
                            <i className="lock icon"></i>
                        </div>
                        </div>
                        <button className="fluid ui violet button" onClick = {async() => 
                            {this.CheckCreds(this.state.username, this.state.password, this.state.firstname, this.state.lastname)}}>
                                SignUp
                        </button>
                    </div>
                    </div>
                </div>
            </>

        ) 

    }



}



/*function SignUp() {

    /**
     * Local variables keeping track of user input 
     */
    /*const [u_username, setUsername] = useState("");
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
                <button className="fluid ui violet button" onClick = {async() => CheckCreds(u_username, u_password, u_firstname, u_lastname)}>SignUp</button>
            </div>
            </div>
        </div>
    </>
    )

}

async function CheckCreds(u_username, u_password, u_firstname, u_lastname) {
    
    const result = await fetch('/open_api/signup', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
    },
        body: JSON.stringify({username: u_username, password: u_password, firstname: u_firstname, lastname: u_lastname})
    })
    .then(res => res.json())
    
    
    if (!(result.authenticated)) {
        alert("Username is already taken. Please try again");
    }
    else {
        alert("Succes! You will now be redirected to the next page");
    }
}*/ 



export {SignUp}