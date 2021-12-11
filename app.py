import time
import tweepy

CONSUMER_KEY = 'ZpCvFn5OeojLLZVCOURayaIJY'
CONSUMER_SECRET = 'VDfPkTfUZ74dGHEScdeYXJUdN2I2PVrAufLCUc0awWVggffiI6'
ACCESS_KEY = '1285604668991660032-gVTXHHRlP2r4Kt6mVgyE6TtLbGtAbD'
ACCESS_SECRET = 'xCIQTvv4ZSl1H2cdaxVK8KyUMV3P7xuEL0ouLWNuxstWp'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

S = "#helloworld"


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def auto():
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if S.lower() in mention.full_text.lower():
            print('found it')
            print('responding back...')

            api.retweet(mention.id)
            api.create_favorite(mention.id)

            time.sleep(10)


while True:
    auto()
    time.sleep(30)
