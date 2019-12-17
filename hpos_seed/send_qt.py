from hpos_seed.send import send
from pathlib import Path
from PyQt5.QtCore import QObject, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
from twisted.internet.defer import inlineCallbacks
import sys
import wormhole


base_path = Path(__file__).parent
qml_path = (base_path / 'send_qt.qml').resolve()


class App(QObject):
    def __init__(self):
        QObject.__init__(self)

    success = pyqtSignal()

    @pyqtSlot(str, result=str)
    def file_url_name(self, file_url):
        return QUrl(file_url).fileName()

    @pyqtSlot(str, result=bool)
    def is_valid_wormhole_code(self, wormhole_code):
        try:
            wormhole._code.validate_code(wormhole_code)
            return True
        except wormhole.errors.KeyFormatError:
            return False

    @inlineCallbacks
    @pyqtSlot(str, str)
    def send(self, wormhole_code, config_file_url):
        config_path = QUrl(config_file_url).toLocalFile()
        with open(config_path) as f:
            yield send(wormhole_code, f.read(), reactor)
            self.success.emit()


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    qapp.setApplicationName("HPOS Seed")
    qapp.setOrganizationDomain("holo.host")
    qapp.setOrganizationName("Holo")

    # qt5reactor needs to be imported and installed after QApplication(),
    # but before importing twisted.internet.reactor. See qt5reactor docs.
    import qt5reactor
    qt5reactor.install()

    app = App()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("app", app)
    engine.load(str(qml_path))

    from twisted.internet import reactor

    reactor.run()
