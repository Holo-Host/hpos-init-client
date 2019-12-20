import QtQuick 2.12
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.12

ApplicationWindow {
    property var configFileUrl: null
    property bool success

    visible: true
    width: 400
    title: qsTr("HPOS Seed")
 
    DropArea {
        anchors.fill: parent

        onDropped:
            configFileUrl = drop.text.trim()
    }

    GridLayout {
        id: layout

        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right

        anchors.topMargin: 20
        anchors.leftMargin: 20
        anchors.rightMargin: 30
 
        columns: 3
        columnSpacing: 10
        rowSpacing: 10

        Label {
            text: qsTr("Config:")

            Layout.alignment: Qt.AlignRight
        }

        // GtkFileChooserButton emulation:
        // https://developer.gnome.org/gtk3/stable/GtkFileChooserButton.html
        Button {
            id: configPath 
            iconName: "document-open"
            text: " " + (configFileUrl ? app.file_url_name(configFileUrl): "N/A")

            Layout.columnSpan: 2
            Layout.fillWidth: true
   
            onClicked:
                fileDialog.open()

            FileDialog {
                id: fileDialog

                nameFilters: [
                    qsTr("HPOS config files (hpos-config.json)"),
                    qsTr("All files (*)")
                ]
   
                onAccepted:
                    configFileUrl = fileDialog.fileUrl
            }
        }

        Label {
            text: qsTr("Code:")

            Layout.alignment: Qt.AlignRight
        }
 
        TextField {
            id: wormholeCode

            Layout.columnSpan: 2
            Layout.fillWidth: true
        }

        Label {}

        Label {
            id: status
            text: success ? "✔️" : ""

            horizontalAlignment: Text.AlignRight
            Layout.fillWidth: true
        }
 
        Button {
            id: send
            enabled: configFileUrl !== null && app.is_valid_wormhole_code(wormholeCode.text)
            isDefault: true
            text: qsTr("Send")

            onClicked: {
                success = false
                app.send(wormholeCode.text, configFileUrl)
            }
        }

        Row {
            Layout.columnSpan: layout.columns
            Layout.fillWidth: true
            Layout.preferredHeight: layout.anchors.topMargin - layout.rowSpacing
        }
    }

    Connections {
        target: app

        onSuccess:
            success = true
    }
}
