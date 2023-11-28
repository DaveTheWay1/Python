from flask_app.models import tweet
from flask_app import app
from flask import render_template, redirect, session, request

@app.route('/tweet/create', methods=["POST"])
def createTweet():
    # * we check to see if the user is in session. 
    # * in other words if a user is logged in.
    # * if they are not they will not be granted
    # * to the page but sent back to login/register
    if "user_id" not in session:
        return redirect('/')
    
    # * everything from this point foward is with a user
    # * being logged in.

    # * we check to see is the tweet the user
    # * created is valid.
    if tweet.Tweet.validate_tweet(request.form):
        # * if it is then we will store all the
        # * input into a dictiory called data.
        data = {
            "content": request.form['content'],
            "location": request.form['location'],
            # * we don't do a request.form here. 
            # * for the user_id, rather we pass in 
            # * the user in session which should
            # * the user creating the post anyway
            "user_id": session['user_id']
        }
        # * as long as the validate tweet passes
        # * and the data is passed corretly
        # * then we will save the tweet
        # * passing in the data dictionary
        tweet.Tweet.save(data)
        # * if all is succesful then the user
        # * gets passed into the proper page
        return redirect('/dashboard')
    # * if the tweet fails the user gets redirected
    # * back to the create tweet page
    return redirect('/tweet')