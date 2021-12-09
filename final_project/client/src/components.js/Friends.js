import React, {Component} from 'react';
import {AddFriend} from './AddFriend';
import {SignUp} from './SignUp';
import Cookies from 'js-cookie';
import { secure_get_with_token } from './cis444';

class Friends extends Component {

    constructor() {
        super();
        this.state = {
            friendlist: null,
            json_response: null,
            addfriendinputvisible: false,
            displayFriendList: false,
        }
        
    }

    setActiveRow(id) {
        this.setState({
            selectedrowid: id
        });
    }

    async GetFriendList() {
        
        secure_get_with_token(await fetch('/secure_api/getfriends', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': Cookies.get('jwt')
            },
            body: JSON.stringify({text: 'text'})
        })
        .then((response) => response.json())
        .then((json) => this.setState({json_response: json})))
        
        console.log(this.state.json_response.friends);
        
        this.friendlist = this.state.json_response.friends;


        if ((this.friendlist).length > 0) {
            this.setState({displayFriendList: true})
        }

    }



    render() {

        /*const FriendList = () => this.state.displayFriendList ? this.friendlist.map((friends)=> 
            <li key = {friends.id}><button>{friends}</button></li> ) : null */

        
        const FriendList = () => this.state.displayFriendList ? this.friendlist.map((friends) => 
            <div class="ui segments" key = {friends.id}>
                <button class = "ui inverted basic button friendbutton">{friends}</button>
            </div> ) : null

        
        return (
            <>
                <button className = "ui inverted button" onClick = {async() => {this.GetFriendList()}}>View Friend List</button>
                <div class="ui segments"><FriendList/></div>
            </>
        )
    }

}

export {Friends}