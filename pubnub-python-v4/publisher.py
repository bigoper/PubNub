from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

# PubNub config section
pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'demo'
pnconfig.publish_key = 'demo'
pnconfig.uuid = 'publisher-uuid'
# PubNub Init (v4)
pubnub = PubNub(pnconfig)

myChannel = "myDemoChannel"

# User Defined PubNub CallBack Function
def publish_callback(result, status):
    print('publish_callback: result {}'.format(result))
    print('publish_callback: status {}'.format(status))
    pass

# The data/info to be published to the channel
data = {
    'text': "Some demo data.."
}

pubnub.publish().channel(myChannel).message(['data', data]).async(publish_callback)