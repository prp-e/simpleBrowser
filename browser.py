import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("Simple Browser")
goButton = QPushButton("Go")
navBar = QLineEdit()
webView = QWebView()
hbox1 = QHBoxLayout()
hbox2 = QHBoxLayout()
vbox = QVBoxLayout()
hbox1.addWidget(navBar)
hbox1.addWidget(goButton)
hbox2.addWidget(webView)
vbox.addLayout(hbox1)
vbox.addLayout(hbox2)
win.setLayout(vbox)
def browse():
    webView.setUrl(navBar.text())

goButton.clicked.connect(browse)
win.show()
app.exec_()
sys.exit()
