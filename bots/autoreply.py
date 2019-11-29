#!/usr/bin/env python
# QuestGiver/bots/autoreply.py

import tweepy
import logging
from config import create_api
from questmaker import Request
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

quests = Request()

def check_mentions(api, keywords, since_id, check_time):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id, tweet_mode='extended').items():
        new_since_id = max(tweet.id, new_since_id)
        logger.info(f"Tweet mention created on {tweet.created_at}")
        if tweet.created_at.timestamp() < check_time:
            continue
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.full_text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            #if not tweet.user.following:
            #    tweet.user.follow()

            api.update_status(
            #    status="Please reach us via DM",
                status=make_reply(tweet, quests.generate_new_quest()),
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def make_reply(tweet, message):
    status = "@" + tweet.user.screen_name + " "
    status += message
    return status

# def convert_time(tweet):
#     ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
#     ts = time.mktime(ts)
#     return ts

def main():
    api = create_api()
    since_id = 1
    check_time = time.time()
    
    while True:
        since_id = check_mentions(api, ["quest", "task"], since_id, check_time)
        check_time = time.time()
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()