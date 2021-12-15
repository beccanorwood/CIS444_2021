import React, {Component} from 'react';
import Cookies from 'js-cookie';
import { secure_get_with_token } from './cis444';
import { AddFriend } from './AddFriend';
import { JoinRoom } from './JoinRoom';

class Friends extends Component {

    constructor() {
        super();
        this.state = {
            friendlist: [],
            restaurantlist: [],
            visible: true,
            json_response: null,
            joinRoomVisible: false,
            friendListVisible: false,
            displayFriendList: false
        }
        this.friendSelected = this.friendSelected.bind(this);
        this.setJoinRoomVisible = this.setJoinRoomVisible.bind(this);
    }

    friendSelected(e) {
        this.setState({
            [e.target.name]: e.target.value
        });

        this.setJoinRoomVisible();
    }

    setJoinRoomVisible() {
        this.setState({joinRoomVisible: true})
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
        
    
        this.friendlist = this.state.json_response.friends;


        if ((this.friendlist).length >= 0) {
            this.setState({displayFriendList: true})
            this.setState({friendListVisible: true})
        }

    }

    render() {

        /*const FriendList = () => this.state.displayFriendList ? this.friendlist.map((friends) => 
                <button key = {friends.id} className = "ui inverted basic button friendbutton">{friends}</button>) : null */
        
        const FriendList = () => this.state.displayFriendList ? this.friendlist.map((friends) => 
        <div className="ui segments" key = {friends.id}>
            <button className = "ui inverted fluid basic button friendbutton" name = "friend_name" value = {friends} onClick = {this.friendSelected}>{friends}</button>
        </div> ) : null;

        if (this.state.joinRoomVisible) {

            return (
                <JoinRoom friend_name = {this.state.friend_name}/>
            )
        }

        else {
        
            return (
                <>
                    <button className = "ui inverted button" onClick = {async() => {this.GetFriendList()}}>View Friends</button>
                    <div className="ui segments"><FriendList/></div>
                </>
            )

        }
    }

}

export {Friends}