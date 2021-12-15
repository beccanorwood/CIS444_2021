import React, {useState, useEffect, useRef, useMemo} from 'react';
import { secure_get_with_token } from './cis444'
import TinderCard from 'react-tinder-card';
import Cookies from 'js-cookie';


const imgs = [
    {
        name: "BJ's Restaurant and Brewhouse",
        url:  "https://idunno-images.s3.amazonaws.com/idunno_restaurants/BJsRestaurant_450x450.jpeg"
    },
    {
        name: 'Chick-fil-A',
        url: "https://idunno-images.s3.amazonaws.com/idunno_restaurants/Chick_fil_A_450x450.jpg"
    },
    {
        name: "Denny's",
        url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/Dennys_450x450.jpg'
    },
    {
        name: 'Jack in the Box',
        url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/JackintheBox_450x450.jpg'
    },
    {
        name: "McDonalds",
        url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/McDonalds_450x450.jpg'
    },
    {
        name: "P.F. Changs",
        url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/P.F._Chang_450x450.jpg'
    },
    {
        name: 'Panda Express',
        url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/Panda_Express_450x450.png'
    },
    {
        name: 'Red Lobster',
        url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/RedLobster_450x450.jpg'
    },
    {
        name: 'The Cheesecake Factory',
        url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/TheCheesecakeFactory_450x450.jpg'
    },
    {
        name: "Wendy's",
        url:  'https://idunno-images.s3.amazonaws.com/idunno_restaurants/Wendys_450x450.jpg'
    }
]


function Simple() {
  const characters = imgs
  const [lastDirection, setLastDirection] = useState()


  const [json, setJSON] = useState(); //response from inserting matches
  const [matchjson, setMatchJSON] = useState();

  const [result, setMatchResult] = useState();

  const swiped = (direction, nameToDelete) => {
    console.log('removing: ' + nameToDelete)
    setLastDirection(direction)

    APITest(direction, nameToDelete)
  }

  const outOfFrame = (name) => {
    console.log(name + ' left the screen!')
  }

  const APITest = async (dir, name) => {

    secure_get_with_token(await fetch('/secure_api/input_swiped', {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': Cookies.get('jwt')
      },
      body: JSON.stringify({direction: dir, restaurantname: name})
    })
    .then((response) => response.json())
    .then((json) => setJSON(json))
    )

  }

  //API call to check matches after time elapsed 
  useEffect(() => {

      const CheckMatches = setTimeout(() => {
            secure_get_with_token(fetch('/secure_api/checkmatches', {
              method: "POST",
              headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': Cookies.get('jwt')
              },
            })
            .then((response) => response.json())
            .then((json) => setMatchJSON(json))
            )

            //Check if valid json response was returned to stop infinite loop
            if (matchjson) {
              //Check if match was found, if not keep calling function 
              if (matchjson.message) {
                alert("Match Found!");
                alert(matchjson.matches)
                setMatchResult(matchjson);
              }
              else {
                alert("No match Found!");
              }
            }
        
          }, 5000);
        }
    )


  return (
    <div>
      <link href='https://fonts.googleapis.com/css?family=Damion&display=swap' rel='stylesheet' />
      <link href='https://fonts.googleapis.com/css?family=Alatsi&display=swap' rel='stylesheet' />
      <h1>iDunno?</h1>
      <div className='cardContainer'>
        {characters.map((character) =>
          <TinderCard className='swipe' key={character.name} onSwipe={(dir) => swiped(dir, character.name)} onCardLeftScreen={() => outOfFrame(character.name)}>
            <div style={{ backgroundImage: 'url(' + character.url + ')' }} className='card'>
              <h3>{character.name}</h3>
            </div>
          </TinderCard>
        )}
      </div>
      {lastDirection ? <h2 className='infoText'>You swiped {lastDirection}</h2> : null}
    </div>
  )
}

export {Simple}
