To boostrap this project::

    git clone https://github.com/chrischambers/octocount.git
    cd octocount
    mkvirtualenv octocount
    pip install -r requirements/dev.txt

To run the tests::

    ./runtests.sh

To run the development server locally::

    ./app.py

So far I've spent approximately 5.5 hours playing around with this, and
probably a couple of hours reading about tornado. It's definitely an
interesting framework, though deploying via GAE seems to negate a lot of the
main benefits that Tornado provides over, say, Django or Flask.
(http://www.tornadoweb.org/en/stable/guide/running.html#wsgi-and-google-app-engine)

Despite my lack of familiarity, this project is a good indication of my
general style: very thin controllers which delegate most of their thinking to
smarter domain objects, which are unit tested independently. I've used the
specification style of testing, which I prefer. Ordinarily I'd also setup
acceptance tests which drive a browser at the endpoints to make sure they are
behaving, but being unfamiliar with tornado I've deferred that.
