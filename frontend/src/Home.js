import React, { useState,useEffect } from 'react'
import './gift.css';
import axios from 'axios'
import chatbox from "./app1"
import myImage from './image/chatbox-icon.svg'; 
import myImage2 from './image/dd.png'; 
function Home() {
    const[author, setAuthor]= useState('') 
    const[comment, setComment]= useState('')
    // const [errors,setErrors]= useState({})
    const handleInput = (event) => {
        if(event.target.name==="author"){
            setAuthor(event.target.value);
        }else{
            setComment(event.target.value)
        }
    };
    const handleSubmit=(event)=>{
        event.preventDefault();
        axios.post('/home', {author:author,comment:comment})
        .then(res=>{
            console.log(res)
            setAuthor('')
            setComment('')
        })
        .catch(err=>console.log(err));
    }
    useEffect(() => {
      // Initialize and display the chatbox when the component mounts
      const chatboxInstance = new chatbox();
      chatboxInstance.display();
    }, []);
    // useEffect(() => {
    // // console.log(values);
    // }, [values]);
    return (
        <div>
            <div id="p1">
                <h1 id="tag1">Uber Trips ML/Project</h1>
                <h3 id="tag2">"Where Uber Journeys Begin and Unforgettable Memories Await!"</h3>
            </div>
            <div id="p2">
                <div id="h12">
                    <h2 id="ac1">Top 3 Reasons to Choose Uber for Your Next Journey</h2>
                </div>
                <div id="p2-warp">
                    <div id="ac21">
                        <img id="img-1" src="https://www.ridester.com/wp-content/uploads/2018/08/schedule_uber_2.webp" />
                        <h3>Reliability and Convenience:</h3>
                        <p>Enjoy stress-free travel with Uber's reliable and convenient rides, available at your fingertips for any destination.</p>
                    </div>
                    <div id="ac21">
                        <img id="img-1" src="https://icon-library.com/images/cost-icon/cost-icon-6.jpg" />
                        <h3>Enjoy Local Cuisine</h3>
                        <p>Experience clarity in costs with upfront pricing, fare estimates, and seamless, predictable payments through the Uber app.</p>
                    </div>
                    <div id="ac21">
                        <img id="img-1" src="https://onlineandyou.com/wp-content/uploads/2020/05/UBER.jpg" />
                        <h3>Safety First:</h3>
                        <p>Prioritize safety with real-time tracking, detailed driver information, and community-driven feedback for a secure Uber journey.</p>
                    </div>
                </div>
            </div>
            <div id="p3">
                <div id="ag1">
                    <img id="gd" src={myImage2}/>
                    <div id="abgd">
                        <h2>Your friendly Chat-bot</h2>
                        <p>
                        "Introducing our Chat Bot - your virtual automotive advisor! Seamlessly aiding you in choosing the perfect vehicle based on your location, this intuitive assistant ensures you make the best transportation decision wherever you go."
                        </p>
                        <h3>Sam</h3>
                    </div>
                </div>
            </div>
            <form action="" onSubmit={handleSubmit}>
                <div id="p4">
                    <div className="mb-3">
                        <input
                        type="text"
                        className="form-control"
                        placeholder="Author"
                        name='author'
                        value={author}
                        onChange={handleInput}
                        />
                    </div>
                    <div className="mb-3">
                        <textarea
                        className="form-control"
                        placeholder="Comment"
                        name='comment'
                        value={comment}
                        onChange={handleInput}
                        ></textarea>
                    </div>
                    <button type="submit" className="btn btn-primary">
                        Post Comment
                    </button>
                </div>
        </form>
        <div class="chatbox">
          <div class="chatbox__support">
              <div class="chatbox__header">
                  <div class="chatbox__image--header">
                      <img src="https://img.icons8.com/color/48/000000/circled-user-female-skin-type-5--v1.png" alt="image"></img>
                  </div>
                  <div class="chatbox__content--header">
                      <h4 class="chatbox__heading--header">Chat support</h4>
                      <p class="chatbox__description--header">Hi. My name is Sam. How can I help you?</p>
                  </div>
              </div>
              <div class="chatbox__messages">
                  <div></div>
              </div>
              <div class="chatbox__footer">
                  <input type="text" placeholder="Write a message..."></input>
                  <button class="chatbox__send--footer send__button">Send</button>
              </div>
          </div>
          <div class="chatbox__button">
              <button><img src={myImage} /></button>
          </div>
      </div>
        </div>
    );
}

export default Home