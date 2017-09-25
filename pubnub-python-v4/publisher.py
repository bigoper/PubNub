from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

import sys

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'demo'
pnconfig.publish_key = 'demo'
pnconfig.uuid = 'publisher-uuid'
pubnub = PubNub(pnconfig)

def publish_callback(result, status):
    print('my_publish_callback');
    pass

data = {
    'text': "Some demo data.."
}
# envelope = pubnub.set_state().channels(['myDemoChannel']).state(my_msg).sync()

pubnub.publish().channel('myDemoChannel').message(['data', data]).async(publish_callback)