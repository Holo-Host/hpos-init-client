import wormhole


ACK_MESSAGE = wormhole.util.dict_to_bytes({"ack": True})
WORMHOLE_APPID = 'holo.host/hpos-seed/v1'
WORMHOLE_RELAY_URL = 'ws://relay.magic-wormhole.io:4000/v1'
