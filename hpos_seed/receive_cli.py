from hpos_seed.receive import receive
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import sys


def on_wormhole_code(wormhole_code):
    print("Wormhole code:", wormhole_code, file=sys.stderr)


@inlineCallbacks
def main():
    message = yield receive(on_wormhole_code, reactor)
    print(message)

    reactor.callLater(0, reactor.stop)


if __name__ == '__main__':
    reactor.callLater(0, main)
    reactor.run()
