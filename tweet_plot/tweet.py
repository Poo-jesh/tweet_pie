import twitter
from nltk.tokenize import TweetTokenizer
import os


def Analyzer(text):
    # your twitter api detail

    cons_key = ''
    cons_secret = ''
    access_token_key = ''
    access_token_secret = ''

    api = twitter.Api(
        consumer_key=cons_key,
        consumer_secret=cons_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret,
    )

    try:
        statuses = api.GetUserTimeline(screen_name=text, since_id=100)
    except Exception as err:
        return ["twitter_err"]
    file_pos = open(os.path.join(os.getcwd(), "tweet_plot\\positive-words.txt"), "r")
    file_pos_set = set()

    for word in file_pos:
        file_pos_set.add(word.rstrip('\n'))
    file_pos.close()

    file_neg = open(os.path.join(os.getcwd(), "tweet_plot\\negative-words.txt"), "r")
    file_neg_set = set()

    for word in file_neg:
        file_neg_set.add(word.strip('\n'))
    file_neg.close()

    pos = 0
    neg = 0
    nut = 0
    tweet_token = TweetTokenizer()

    for words in statuses:
        tokens = tweet_token.tokenize(words.text)
        scor = 0
        for tweets in tokens:
            if tweets.lower() in file_pos_set:
                scor += 1
            elif tweets.lower() in file_neg_set:
                scor -= 1
            else:
                continue
        if scor > 0:
            pos += 1
        elif scor < 0:
            neg += 1
        else:
            nut += 1
    return [pos, neg, nut]
