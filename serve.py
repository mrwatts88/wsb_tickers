from flask import Flask
from reddit_client import RedditClient
from aggregator import Aggregator

app = Flask(__name__)
aggregator = Aggregator(300)
client = RedditClient(aggregator)

aggregator.start_aggregating()
client.start_streaming()

@app.route('/')
def hello_world():
    return aggregator.get_output()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
