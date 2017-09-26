# PubNub

## SDK-Python V4
[![Build Status](https://travis-ci.org/pubnub/python.svg?branch=master)](https://travis-ci.org/pubnub/python)
[![codecov](https://codecov.io/gh/pubnub/python/branch/master/graph/badge.svg)](https://codecov.io/gh/pubnub/python)
[![PyPI](https://img.shields.io/pypi/v/pubnub.svg)](https://pypi.python.org/pypi/pubnub/)
[![PyPI](https://img.shields.io/pypi/pyversions/pubnub.svg)](https://pypi.python.org/pypi/pubnub/)
[![Docs](https://img.shields.io/badge/docs-online-blue.svg)](https://www.pubnub.com/docs/python/pubnub-python-sdk-v4)

### Environment Setup (optional)
- https://virtualenv.pypa.io/en/stable/

### Pre-requisits
As documented in our [Online Documentation](https://www.pubnub.com/docs/python/pubnub-python-sdk#how_to_get_it)

```pip install 'pubnub>=4.0.13'```

### PubSub Demo
![alt text][publish] ![alt text][subscribe]

#### publisher.py
This our publisher entity, we'll use it to publish messages to a channel.

`python publisher.py`

#### subscriber.py
This is our subscriber entity, we'l use it to subscribe/register to a channel and listen to published messages.

`python subscriber.py`

> NOTE: for more info please visit our [Python V4 Publish/Subscribe Tutorial for Realtime Apps](https://www.pubnub.com/docs/python/data-streams-publish-and-subscribe)

[subscribe]: https://www.pubnub.com/static/images/old/pubnub-pulse-1.gif "PubNub Subscribe"
[publish]: https://www.pubnub.com/static/images/old/pubnub-galaxy.gif "PubNub Publish"