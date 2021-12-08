import React, {useState, useEffect, Component} from 'react';
import {secure_get_with_token} from './cis444';
import Cookies from 'js-cookie';

class AddFriend extends Component {

    constructor() {
        super();
        this.state = {
            json_response: null,
            visible: true,
            inputfriendvisible: false,
            joinroomvisible: false
        }
        this.onInputChange = this.onInputChange.bind(this);
        this.onAddFriendClick = this.onAddFriendClick.bind(this);
        this.onInputFriendUsername = this.onInputFriendUsername.bind(this);
    }


    onInputChange(e) {
        this.setState({
            [e.target.name]: e.target.value
        });
    }

    onInputFriendUsername() {
        console.log("On Input Friend Username: " + this.state);
        this.setState({joinroomvisible: true});
    }

    onAddFriendClick() {
        this.setState({inputfriendvisible: true});
    }


    async CheckFriendUsername(friendusername) {

        secure_get_with_token(await fetch('/secure_api/addfriend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': Cookies.get('jwt')
            },
            body: JSON.stringify({friendusername: friendusername}), function(data) {
                console.log(data);
            }
            })
            .then((response) => response.json())
            .then((json) => this.setState({json_response: json})));
        

            console.log(this.state.json_response);
            console.log(this.state.json_response.valid);


            if (!(this.state.json_response.valid)) {
                alert("User does not exist, Try again!");
            }
            else {
                alert('Success! You will be redirected to your room shortly!');
                this.setState({visible: false});
            }
    
    }


    render() {

        const JoinRoom = () => <button className="ui violet button">Join Room</button>

        //const buttonText = this.state.inputfriendvisible ? "Input Friend Username" : "Add Friend";
        //const buttonsubText = this.state.inputfriendvisible ? "" : "Click Here!";

        if (this.state.joinroomvisible) {
            return <div><JoinRoom/></div>
        }

        else return (

            <div className="ui input">
                <input type="text" placeholder="Friend Username" name ="friendusername" value = {this.state.name} onChange = {this.onInputChange}/>
                <button className = "fluid ui violet button" onClick = {async() => this.CheckFriendUsername(this.state.friendusername)}>Add Friend</button>
            </div>
        )

    }

}


export {AddFriend}