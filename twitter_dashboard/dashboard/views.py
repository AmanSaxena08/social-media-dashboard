from django.shortcuts import render
import os
import requests
from dotenv import load_dotenv

from dotenv import load_dotenv
load_dotenv()

# Load environment variables
load_dotenv()

# Get Twitter Bearer Token from .env
TWITTER_BEARER_TOKEN = os.getenv("your_real_bearer_token_here")

# Function to fetch tweets
def get_tweets(username):
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}

    # Get user ID by username
    user_url = f"https://api.twitter.com/2/users/by/username/{username}"
    user_resp = requests.get(user_url, headers=headers)

    # ✅ STEP 1: Debug print
    print("USER RESPONSE JSON:", user_resp.json())

    # Error handling for user lookup
    if user_resp.status_code != 200 or 'data' not in user_resp.json():
        return [], f"Error fetching user: {user_resp.json()}"

    user_id = user_resp.json()['data']['id']

    # Get user's tweets
    tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    tweets_resp = requests.get(tweets_url, headers=headers)

    # Error handling for tweets fetch
    if tweets_resp.status_code != 200:
        return [], f"Error fetching tweets: {tweets_resp.json()}"

    return tweets_resp.json().get('data', []), None

# Home view to display tweets
def home(request):
    username = "TwitterDev"  # Default Twitter username
    tweets, error = get_tweets(username)
    return render(request, "dashboard/home.html", {
        "tweets": tweets,
        "username": username,
        "error": error
    })

# Profile page view
def profile(request):
    return render(request, "dashboard/profile.html")
