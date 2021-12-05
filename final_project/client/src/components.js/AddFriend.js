import React, {useState, useEffect} from 'react';

const AddFriend = () => {

    const [showFriendForm, setShowFriendForm] = useState(false);
    const onClick = () => {
        setShowFriendForm(true);
    }

    return showFriendForm ?
    <FriendUsername/>
    : (
        <>
            <div className="ui blue inverted circular segment">
                <h2 button className="ui header" onClick = {onClick}>
                    Add Friend
                <div className="sub header">Click Here!</div>
                </h2>
            </div>
        </>
    )

}

/**
 * Simple Button Component that displays when user's enters friend username
 */
const JoinRoom = () => <button className="ui violet button">Join Room</button>


const FriendUsername = () => {

    const [showJoinRoomButton, setShowJoinRoomButton] = useState(false);
    const onClick = () => {
        setShowJoinRoomButton(true);
    }

    return showJoinRoomButton ?
    <JoinRoom/>
    : (
        <>
            <div class="ui input">
                <input type="text" placeholder="Search..."/>
                <button className = "fluid ui violet button" onClick = {onClick}>Submit</button>
            </div>
        </>
    )
}

/**
 * On button press, will ask user to input friend's username 
 */
/*async function SectionButtonTest() {
    alert('It Worked!');
}*/


/**
 * If valid username is sent to API, user has option to join room 
 */


export {AddFriend}