import React, {Component} from 'react';
import {secure_get_with_token} from './cis444';
import { Simple } from './Restaurants';
import Cookies from 'js-cookie';

class JoinRoom extends Component {

    constructor() {
        super();
        this.state = {
            json_response: "",
            visible: true,
            showRestaurants: false
        }
    }

    /**
     * API call to test email request to other user 
     */
    async startSession(friend_name) {

        secure_get_with_token(await fetch('/secure_api/joinroom', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': Cookies.get('jwt')
            },
            body: JSON.stringify({friendusername: friend_name})
        })
        .then((response) => response.json())
        .then((json) => this.setState({json_response: json}))
        )

        if (this.state.json_response.status === 200) {
            this.setState({showRestaurants: true});
        }

    }


    render() {

        if (this.state.showRestaurants) {
            return <div><Simple/></div>
        }

        return (
            
            <button className="ui violet button" onClick = {async () => this.startSession(this.props.friend_name)}>Start Session</button>
        
        )
    }

}

export {JoinRoom}