import React, {useState, useEffect, Component} from 'react';
import ReactDOM from 'react-dom';
import {AddFriend} from './AddFriend';
import {SignUp} from './SignUp';




class UserAuth extends Component {

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


    //Method to call flask_api to check login credentials
    async CheckCreds(u_username, u_password) {

        //API call sends a json object to the server and receives one in response 

        const response = await fetch('/open_api/login', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        },
            body: JSON.stringify({username: u_username, password: u_password})
        })
        .then(res => res.json())

        
        if (!(response.authenticated)) {
            alert("Incorrect credentials. Try again!");
        }
        else {
            alert("Success! You will now be redirected!");
            this.setState({visible: false});
        }

    }



    render() {

        if (!this.state.visible) {
            return <div><AddFriend/></div>   
        }
        
        else {
                return (
                <>
                    <div className="ui placeholder segment">
                        <div className="ui two column very relaxed stackable grid">
                            <div className="column">
                            <div className="ui form">
                                <div className="field">
                                <label>Username</label>
                                <div className="ui left icon input">
                                    <input type="text" placeholder="Username" name ="username" value = {this.state.name} onChange={this.onInputChange}/>
                                    <i className="user icon"></i>
                                </div>
                                </div>
                                <div className="field">
                                <label>Password</label>
                                <div className="ui left icon input">
                                    <input type="password" name = "password" value = {this.state.name} onChange={this.onInputChange}/>
                                    <i className="lock icon"></i>
                                </div>
                                </div>
                                <button className="fluid ui violet button" onClick = {async() => {this.CheckCreds(this.state.username, this.state.password)}}>Login</button>
                            </div>
                            </div>
                            <div className="middle aligned column">
                            <div className="ui big button">
                                <i className onClick = "signup icon"></i>
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

    }

}


export {UserAuth};