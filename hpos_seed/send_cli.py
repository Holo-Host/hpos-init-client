from hpos_seed.send import send
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import sys


@inlineCallbacks
def main():
    try:
        _, wormhole_code, config_path = sys.argv
        with open(config_path) as f:
            yield send(wormhole_code, f.read(), reactor)
        reactor.callLater(0, reactor.stop)
    except ValueError:
        print("Usage: {} <wormhole_code> <config_path>".format(
            sys.argv[0]), file=sys.stderr)
        reactor.callLater(1, reactor.stop)


if __name__ == '__main__':
    reactor.callLater(0, main)
    reactor.run()
