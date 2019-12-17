from hpos_seed import ACK_MESSAGE, WORMHOLE_APPID, WORMHOLE_RELAY_URL
from twisted.internet.defer import inlineCallbacks
import wormhole


@inlineCallbacks
def receive(on_wormhole_code, reactor):
    w = wormhole.create(WORMHOLE_APPID, WORMHOLE_RELAY_URL, reactor)
    w.allocate_code()

    wormhole_code = yield w.get_code()
    yield on_wormhole_code(wormhole_code)

    data_message = yield w.get_message()
    data = wormhole.util.bytes_to_dict(data_message)['data']

    yield w.send_message(ACK_MESSAGE)
    yield w.close()

    return data
