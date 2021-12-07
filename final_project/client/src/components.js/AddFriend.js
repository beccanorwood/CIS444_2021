import React, {useState, useEffect, Component} from 'react';
import {secure_get_with_token} from './cis444';


class AddFriend extends Component {

    constructor() {
        super();
        this.state = {
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
        this.setState({joinroomvisible: true})
    }

    onAddFriendClick() {
        this.setState({inputfriendvisible: true})
    }


    async CheckFriendUsername(friendusername) {

        const response = secure_get_with_token(fetch('/secure_api/addfriend', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({friendusername: friendusername})
        })
        .then(res => res.json())
        )
      
        if (!response.valid) {
            alert("User does not exist! Try again");
        }
        else {
            alert("Success! You can now begin your food search session");
            this.setState({visible: false});
        }

    }


    render() {

        const JoinRoom = () => <button className="ui violet button">Join Room</button>

        const buttonText = this.state.inputfriendvisible ? "Input Friend Username" : "Add Friend";
        const buttonsubText = this.state.inputfriendvisible ? "" : "Click Here!";

        if (this.state.joinroomvisible) {
            return <div><JoinRoom/></div>
        }

        else return (

            <div className="ui input">
                <input type="text" placeholder="Friend Username" name ="friendusername" value = {this.state.name} onChange = {this.onInputChange}/>
                <button className = "fluid ui violet button" onClick = {this.onInputFriendUsername}>Add Friend</button>
            </div>
        )

    }

}


export {AddFriend}