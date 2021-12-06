import React, {useState, useEffect, useRef, useMemo} from 'react';
import { secure_get_with_token } from './cis444'
import TinderCard from 'react-tinder-card';


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

function Simple () {
    const [currentIndex, setCurrentIndex] = useState(imgs.length - 1)
    const [lastDirection, setLastDirection] = useState()
    // used for outOfFrame closure
    const currentIndexRef = useRef(currentIndex)
  
    const childRefs = useMemo(
      () =>
        Array(imgs.length)
          .fill(0)
          .map((i) => React.createRef()),
      []
    )
  
    const updateCurrentIndex = (val) => {
      setCurrentIndex(val)
      currentIndexRef.current = val
    }
  
    const canGoBack = currentIndex < imgs.length - 1
  
    const canSwipe = currentIndex >= 0
  
    // set last direction and decrease current index
    const swiped = (direction, nameToDelete, index) => {
      setLastDirection(direction)
      updateCurrentIndex(index - 1)
    }
  
    const outOfFrame = (name, idx) => {
      console.log(`${name} (${idx}) left the screen!`, currentIndexRef.current)
      // handle the case in which go back is pressed before card goes outOfFrame
      currentIndexRef.current >= idx && childRefs[idx].current.restoreCard()
      // TODO: when quickly swipe and restore multiple times the same card,
      // it happens multiple outOfFrame events are queued and the card disappear
      // during latest swipes. Only the last outOfFrame event should be considered valid
    }
  
    const swipe = async (dir) => {
      if (canSwipe && currentIndex < imgs.length) {
        await childRefs[currentIndex].current.swipe(dir) // Swipe the card!
      }
    }
  
    // increase current index and show card
    const goBack = async () => {
      if (!canGoBack) return
      const newIndex = currentIndex + 1
      updateCurrentIndex(newIndex)
      await childRefs[newIndex].current.restoreCard()
    }
  
    return (
      <div>
        <link
          href='https://fonts.googleapis.com/css?family=Damion&display=swap'
          rel='stylesheet'
        />
        <link
          href='https://fonts.googleapis.com/css?family=Alatsi&display=swap'
          rel='stylesheet'
        />
        <h1>React Tinder Card</h1>
        <div className='cardContainer'>
          {imgs.map((character, index) => (
            <TinderCard
              ref={childRefs[index]}
              className='swipe'
              key={character.name}
              onSwipe={(dir) => swiped(dir, character.name, index)}
              onCardLeftScreen={() => outOfFrame(character.name, index)}
            >
              <div
                style={{ backgroundImage: 'url(' + character.url + ')' }}
                className='card'
              >
                <h3>{character.name}</h3>
              </div>
            </TinderCard>
          ))}
        </div>
        <div className='buttons'>
          <button style={{ backgroundColor: !canSwipe && '#c3c4d3' }} onClick={() => swipe('left')}>Swipe left!</button>
          <button style={{ backgroundColor: !canGoBack && '#c3c4d3' }} onClick={() => goBack()}>Undo swipe!</button>
          <button style={{ backgroundColor: !canSwipe && '#c3c4d3' }} onClick={() => swipe('right')}>Swipe right!</button>
        </div>
        {lastDirection ? (
          <h2 key={lastDirection} className='infoText'>
            You swiped {lastDirection}
          </h2>
        ) : (
          <h2 className='infoText'>
            Swipe a card or press a button to get Restore Card button visible!
          </h2>
        )}
      </div>
    )
  }

/**
 * API Call to get restaurant images and then return them on screen
 */
function GetImages () {

    //const [response] = await secure_get_with_token(fetch('/secure_api/get_restaurants'));
 
    return (
    <>
        <img src = {"https://idunno-images.s3.amazonaws.com/idunno_restaurants/BJsRestaurant.jpeg"} alt = "" width="100" height = "100"/>
    </>
    )
}

export {Simple}