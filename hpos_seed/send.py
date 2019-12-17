from hpos_seed import ACK_MESSAGE, WORMHOLE_APPID, WORMHOLE_RELAY_URL
from twisted.internet.defer import inlineCallbacks
import wormhole


@inlineCallbacks
def send(wormhole_code, data, reactor):
    w = wormhole.create(WORMHOLE_APPID, WORMHOLE_RELAY_URL, reactor)
    w.set_code(wormhole_code)

    data_message = wormhole.util.dict_to_bytes({'data': data})
    yield w.send_message(data_message)

    ack_message = yield w.get_message()
    assert ack_message == ACK_MESSAGE

    yield w.close()
