import praw
import os
import random

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent="MeowtrixBot"
)

subreddits = ["test", "InternetIsBeautiful", "GlitchArt"]
messages = [
    "🐾 Wake up, Neo. The Meowtrix has you.",
    "😼 Follow the white cat...",
    "✨ Another glitch in the Meowtrix.",
    "🐈‍⬛ Meowtrix is everywhere. https://3069603.github.io/meowtrix/"
]

def post():
    subreddit = reddit.subreddit(random.choice(subreddits))
    title = random.choice(messages)
    subreddit.submit(title=title, selftext="Check out the Meowtrix NFT collection! 🐾✨")

if __name__ == "__main__":
    post()
