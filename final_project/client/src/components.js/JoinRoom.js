import React, {Component} from 'react';
import {secure_get_with_token} from './cis444';
import { Simple } from './Restaurants';
import Cookies from 'js-cookie';

class JoinRoom extends Component {
    constructor() {
        super();
        this.state = {
            json_response: null,
            visible: true,
        }
    }

    /**
     * API call to test email request to other user 
     */
    async startSession() {

        secure_get_with_token(await fetch('/secure_api/joinroom', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': Cookies.get('jwt')
            },
            body: JSON.stringify({text: "test"})
        })
        .then((response) => response.json())
        .then((json) => this.setState({json_response: json}))
        )

        console.log(this.state.json_response);

    }

    render() {

        return (
            
            <button className="ui violet button" onClick = {async () => this.startSession()}>Join Room</button>
            
        )
    }
}

export {JoinRoom}