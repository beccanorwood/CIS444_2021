import React, {useState, useEffect} from 'react';

function AddFriend() {

    return (
    <>
        <div className="ui blue inverted circular segment">
            <h2 className="ui header" onClick = {async() => {SectionButtonTest()}}>
            Add Friend
            <div className="sub header">Click Here!</div>
            </h2>
        </div>
    </>
    )

}

/**
 * On button press, will ask user to input friend's username 
 */
async function SectionButtonTest() {
    alert('It Worked!');
}


/**
 * If valid username is sent to API, user has option to join room 
 */


export {AddFriend}